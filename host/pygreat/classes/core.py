
#
# This file is part of libgreat
#

from ..comms import CommsClass, command_rpc


class CoreAPICommon(CommsClass):
    """
    Class representing the libgreat core API, which all devices must support.
    """

    CLASS_NUMBER = 0
    CLASS_NAME = "core"

    VERB_DESCRIPTOR_OUT_SIGNATURE = 0
    VERB_DESCRIPTOR_IN_SIGNATURE = 1
    VERB_DESCRIPTOR_DOC = 2
    VERB_DESCRIPTOR_OUT_PARAM_NAMES = 3
    VERB_DESCRIPTOR_IN_PARAM_NAMES = 4

    # TODO : move debug into this



class CoreAPI(CoreAPICommon):
    IS_ASYNC = False


class AsyncCoreAPI(CoreAPICommon):
    IS_ASYNC = True



# HACK: XXX: XXX: XXX: XXX:
def __add_sync_async_to_core_classes(sync_async_method_tuple):

    method, async_method = sync_async_method_tuple

    setattr(CoreAPI, method.__name__, method)
    setattr(AsyncCoreAPI, async_method.__name__, async_method)



# RPC that reads the board ID
__add_sync_async_to_core_classes(command_rpc(verb_number=0x0, out_format="<I", name="read_board_id",
        out_parameter_names=["id"], doc=
        """Fetches the board's type identifier.
           A type identifiers uniquely identifies what model of board this is.
        """
    ))


# RPC that reads the version
__add_sync_async_to_core_classes(command_rpc(verb_number = 0x1, out_format="<S",
        name="read_version_string", out_parameter_names=["version"], doc="Fetches the board's version."))

# RPC that reads the part ID
__add_sync_async_to_core_classes(command_rpc(verb_number=0x2, out_format="<2I", name="read_part_id",
        out_parameter_names=["part_id"], doc=
        """Fetches the part ID used on the board.

        Returns:
                A byte-string containing a code that describes which part is used on the board.
        """
    ))

# RPC that fetches the serial number
__add_sync_async_to_core_classes(command_rpc(verb_number=0x3, out_format="<4I",
        name="read_serial_number", out_parameter_names=["serial_number"], doc=
        """Fetches the board's serial number.

        Returns:
            A 4-tuple of uint32's that compose the board's unique serial number.
        """
    ))


# Introspection API.

__add_sync_async_to_core_classes(command_rpc(verb_number=0x4, out_format="<*I",
        name= "get_available_classes", out_parameter_names=["numbers"],
        doc="Fetches the available class numbers."))

__add_sync_async_to_core_classes(command_rpc(verb_number=0x5, in_format="<I", out_format="<*I", name= "get_available_verbs",
        in_parameter_names=["class_number"], out_parameter_names=["numbers"],
        doc="Fetches the available verb numbers for a given class."))

__add_sync_async_to_core_classes(command_rpc(verb_number=0x6, in_format="<II", out_format="<S",
        name= "get_verb_name", out_parameter_names=["name"],
        doc="Fetches the string name for the given verb."))

__add_sync_async_to_core_classes(command_rpc(verb_number=0x7, in_format="<IIB", out_format="<S",
        name= "get_verb_descriptor", out_parameter_names=["descriptor"],
        doc="Fetches the information about the given verb.")) #FIXME: expand docstring

__add_sync_async_to_core_classes(command_rpc(verb_number=0x8, in_format="<I", out_format="<S",
        name= "get_class_name", out_parameter_names=["name"],
        doc="Fetches the string name for the given class."))

__add_sync_async_to_core_classes(command_rpc(verb_number=0x9, in_format="<I", out_format="<S",
        name= "get_class_docs", out_parameter_names=["docstring"],
        doc="Fetches for documentation the given class."))

# FIXME: re-assign verb number or move out of core?
__add_sync_async_to_core_classes(command_rpc(verb_number=0x20, in_format="<I",
        name="request_reset", doc="Resets the relevant board."))


def __set_sync_async_verb_param_gettrs(param_value, param_name, doc):

    def sync_getter(self, class_number, verb_number):
        return self.get_verb_descriptor(class_number, verb_number, param_value)

    async def async_getter(self, class_number, verb_number):
        return await self.get_verb_descriptor(class_number, verb_number, param_value)

    sync_getter.__name__ = async_getter.__name__ = 'get_verb_{}'.format(param_name)

    sync_getter.__doc__ = async_getter.__doc__ = doc

    __add_sync_async_to_core_classes((sync_getter, async_getter))


__param_getters = {
        CoreAPICommon.VERB_DESCRIPTOR_OUT_SIGNATURE: ('out_signature', """ Fetches the given verb's in-signature. """),
        CoreAPICommon.VERB_DESCRIPTOR_IN_SIGNATURE: ('in_signature', """ Fetches the given verb's out-signature. """),
        CoreAPICommon.VERB_DESCRIPTOR_DOC: ('documentation', """ Fetches the given verb's documentation. """),
        CoreAPICommon.VERB_DESCRIPTOR_IN_PARAM_NAMES: ('in_param_names', """ Fetches the given verb's in-param names. """),
        CoreAPICommon.VERB_DESCRIPTOR_OUT_PARAM_NAMES: ('out_param_names', """ Fetches the given verb's out-param names. """)
    }


for param, (name, doc) in __param_getters.items():
    __set_sync_async_verb_param_gettrs(param, name, doc)

