import re
import os
import typing
import json

import artefacts.state
from artefacts.config import conf


RunResults = typing.ForwardRef('RunResults')
Manifest = typing.ForwardRef('Manifest')
Catalog = typing.ForwardRef('Catalog')
Sources = typing.ForwardRef('Sources')


class Artifact:

    @classmethod
    def path(cls):
        """The path to the artifact.
        
        The path is determined by the :ref:`configuration` settings. By default
        artefacts will look in the `./target` directory of the current working 
        directory.
        """
        
        return os.path.join(conf.dbt_target_dir, cls.name() + '.json')

    @classmethod
    def name(cls):
        """The name of the artifact in snake_case.
        """

        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()

    @classmethod
    def load(cls):
        """Load and deserialize the artifact.
        
        The deserialized artifact is cached, so calling this function twice will
        not update the artifact if it has been rebuilt.

        In general, loading the artifacts is not necessary, and most tasks can
        be accomplished by using the :ref:`api` module instead of working with
        the artifact classes directly. 
        """

        if not artefacts.state.exists(cls.name()):
            with open(cls.path(), 'r') as artifact_fh:
                raw_artifact = json.load(artifact_fh)
            artefacts.state.set(cls.name(), cls.parse_obj(raw_artifact))              
        return artefacts.state.get(cls.name())  


class ArtifactReader:

    @property
    def run_results_artifact(self) -> RunResults:
        """A reference to the :class:`RunResults` artifact. """

        return self.get_artifact('run_results')

    @property
    def manifest_artifact(self) -> Manifest:
        """A reference to the :class:`Manifest` artifact. """
        
        return self.get_artifact('manifest')

    @property
    def catalog_artifact(self) -> Catalog:
        """A reference to the :class:`Catalog` artifact. """

        return self.get_artifact('catalog')

    @property
    def sources_artifact(self) -> Sources:
        """A reference to the :class:`Sources` artifact. """

        return self.get_artifact('sources')
    
    def get_artifact(self, artifact_name):
        import artefacts.deserializers

        if artefacts.state.exists(artifact_name):
            return artefacts.state.get(artifact_name)
        else:
            Artifact = {
                'manifest': artefacts.deserializers.Manifest,
                'run_results': artefacts.deserializers.RunResults,
                'sources': artefacts.deserializers.Sources,
                'catalog': artefacts.deserializers.Catalog
            }.get(artifact_name)

            if Artifact is None:
                raise AttributeError(f"Invalid artifact name: {artifact_name}")
            
            return Artifact()


class ArtifactNodeReader(ArtifactReader):
    
    @property
    def manifest(self):
        """A reference to details about the node contained in the manifest."""

        # TODO: what if the resource_type is `source`? I don't think it will
        # show up in the `nodes` reference.
        return self.manifest_artifact.nodes.get(self.unique_id)

    @property
    def catalog(self):
        """A reference to details about the node contained in the catalog."""

        return self.catalog_artifact.nodes.get(self.unique_id)

    @property
    def run_results(self):
        """A reference to results from running the node, if it exists."""

        return [r for r in self.run_results_artifact.results if r.unique_id == self.unique_id]

    @property
    def parents(self):
        """ A list of the node's parents """

        return self.manifest_artifact.parent_map[self.unique_id]

    @property
    def children(self):
        """ A list of the node's children """

        return self.manifest_artifact.child_map[self.unique_id]

    @property
    def tests(self):
        """ A list of any tests that reference the node """

        return [t for t in self.children if t.resource_type == 'test']

    @property
    def snapshots(self):
        """ A list of any snapshots that reference the node """

        return [s for s in self.children if s.resource_type == 'snapshot']