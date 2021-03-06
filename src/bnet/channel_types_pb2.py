# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bnet/channel_types.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bnet.attribute_pb2
import bnet.entity_pb2
import bnet.invitation_types_pb2
import bnet.presence_types_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bnet/channel_types.proto',
  package='bnet.protocol.channel',
  serialized_pb=_b('\n\x18\x62net/channel_types.proto\x12\x15\x62net.protocol.channel\x1a\x14\x62net/attribute.proto\x1a\x11\x62net/entity.proto\x1a\x1b\x62net/invitation_types.proto\x1a\x19\x62net/presence_types.proto\"N\n\x07Message\x12\x35\n\tattribute\x18\x01 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\x12\x0c\n\x04role\x18\x02 \x01(\r\"\xe5\x01\n\x12\x46indChannelOptions\x12\x16\n\x0bstart_index\x18\x01 \x01(\r:\x01\x30\x12\x17\n\x0bmax_results\x18\x02 \x01(\r:\x02\x31\x36\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07program\x18\x04 \x01(\x07\x12\x0e\n\x06locale\x18\x05 \x01(\x07\x12\x15\n\rcapacity_full\x18\x06 \x01(\r\x12\x42\n\x10\x61ttribute_filter\x18\x07 \x02(\x0b\x32(.bnet.protocol.attribute.AttributeFilter\x12\x14\n\x0c\x63hannel_type\x18\x08 \x01(\t\"\x8e\x01\n\x12\x43hannelDescription\x12+\n\nchannel_id\x18\x01 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12\x17\n\x0f\x63urrent_members\x18\x02 \x01(\r\x12\x32\n\x05state\x18\x03 \x01(\x0b\x32#.bnet.protocol.channel.ChannelState\"|\n\x0b\x43hannelInfo\x12>\n\x0b\x64\x65scription\x18\x01 \x02(\x0b\x32).bnet.protocol.channel.ChannelDescription\x12-\n\x06member\x18\x02 \x03(\x0b\x32\x1d.bnet.protocol.channel.Member\"\xd4\x05\n\x0c\x43hannelState\x12\x13\n\x0bmax_members\x18\x01 \x01(\r\x12\x13\n\x0bmin_members\x18\x02 \x01(\r\x12\x35\n\tattribute\x18\x03 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\x12\x38\n\ninvitation\x18\x04 \x03(\x0b\x32$.bnet.protocol.invitation.Invitation\x12\x17\n\x0fmax_invitations\x18\x05 \x01(\r\x12\x0e\n\x06reason\x18\x06 \x01(\r\x12[\n\rprivacy_level\x18\x07 \x01(\x0e\x32\x30.bnet.protocol.channel.ChannelState.PrivacyLevel:\x12PRIVACY_LEVEL_OPEN\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x15\n\rdelegate_name\x18\t \x01(\t\x12\x1d\n\x0c\x63hannel_type\x18\n \x01(\t:\x07\x64\x65\x66\x61ult\x12\x12\n\x07program\x18\x0b \x01(\x07:\x01\x30\x12$\n\x15\x61llow_offline_members\x18\x0c \x01(\x08:\x05\x66\x61lse\x12#\n\x15subscribe_to_presence\x18\r \x01(\x08:\x04true\x12\x34\n\x07\x63hannel\x18\x64 \x01(\x0b\x32#.bnet.protocol.channel.ChannelState\x12\x36\n\x08presence\x18\x65 \x01(\x0b\x32$.bnet.protocol.presence.ChannelState\"\x91\x01\n\x0cPrivacyLevel\x12\x16\n\x12PRIVACY_LEVEL_OPEN\x10\x01\x12,\n(PRIVACY_LEVEL_OPEN_INVITATION_AND_FRIEND\x10\x02\x12!\n\x1dPRIVACY_LEVEL_OPEN_INVITATION\x10\x03\x12\x18\n\x14PRIVACY_LEVEL_CLOSED\x10\x04\"\xae\x01\n\x0bMemberState\x12\x35\n\tattribute\x18\x01 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\x12\x10\n\x04role\x18\x02 \x03(\rB\x02\x10\x01\x12\x15\n\nprivileges\x18\x03 \x01(\x04:\x01\x30\x12(\n\x04info\x18\x04 \x01(\x0b\x32\x1a.bnet.protocol.AccountInfo\x12\x15\n\x06hidden\x18\x05 \x01(\x08:\x05\x66\x61lse\"f\n\x06Member\x12)\n\x08identity\x18\x01 \x02(\x0b\x32\x17.bnet.protocol.Identity\x12\x31\n\x05state\x18\x02 \x02(\x0b\x32\".bnet.protocol.channel.MemberState')
  ,
  dependencies=[bnet.attribute_pb2.DESCRIPTOR,bnet.entity_pb2.DESCRIPTOR,bnet.invitation_types_pb2.DESCRIPTOR,bnet.presence_types_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CHANNELSTATE_PRIVACYLEVEL = _descriptor.EnumDescriptor(
  name='PrivacyLevel',
  full_name='bnet.protocol.channel.ChannelState.PrivacyLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PRIVACY_LEVEL_OPEN', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRIVACY_LEVEL_OPEN_INVITATION_AND_FRIEND', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRIVACY_LEVEL_OPEN_INVITATION', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRIVACY_LEVEL_CLOSED', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1311,
  serialized_end=1456,
)
_sym_db.RegisterEnumDescriptor(_CHANNELSTATE_PRIVACYLEVEL)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='bnet.protocol.channel.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.channel.Message.attribute', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role', full_name='bnet.protocol.channel.Message.role', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=226,
)


_FINDCHANNELOPTIONS = _descriptor.Descriptor(
  name='FindChannelOptions',
  full_name='bnet.protocol.channel.FindChannelOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_index', full_name='bnet.protocol.channel.FindChannelOptions.start_index', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_results', full_name='bnet.protocol.channel.FindChannelOptions.max_results', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=16,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='bnet.protocol.channel.FindChannelOptions.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='program', full_name='bnet.protocol.channel.FindChannelOptions.program', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='locale', full_name='bnet.protocol.channel.FindChannelOptions.locale', index=4,
      number=5, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='capacity_full', full_name='bnet.protocol.channel.FindChannelOptions.capacity_full', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attribute_filter', full_name='bnet.protocol.channel.FindChannelOptions.attribute_filter', index=6,
      number=7, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel_type', full_name='bnet.protocol.channel.FindChannelOptions.channel_type', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=229,
  serialized_end=458,
)


_CHANNELDESCRIPTION = _descriptor.Descriptor(
  name='ChannelDescription',
  full_name='bnet.protocol.channel.ChannelDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='bnet.protocol.channel.ChannelDescription.channel_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_members', full_name='bnet.protocol.channel.ChannelDescription.current_members', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='bnet.protocol.channel.ChannelDescription.state', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=461,
  serialized_end=603,
)


_CHANNELINFO = _descriptor.Descriptor(
  name='ChannelInfo',
  full_name='bnet.protocol.channel.ChannelInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='bnet.protocol.channel.ChannelInfo.description', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='member', full_name='bnet.protocol.channel.ChannelInfo.member', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=605,
  serialized_end=729,
)


_CHANNELSTATE = _descriptor.Descriptor(
  name='ChannelState',
  full_name='bnet.protocol.channel.ChannelState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_members', full_name='bnet.protocol.channel.ChannelState.max_members', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_members', full_name='bnet.protocol.channel.ChannelState.min_members', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.channel.ChannelState.attribute', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='invitation', full_name='bnet.protocol.channel.ChannelState.invitation', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_invitations', full_name='bnet.protocol.channel.ChannelState.max_invitations', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='bnet.protocol.channel.ChannelState.reason', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='privacy_level', full_name='bnet.protocol.channel.ChannelState.privacy_level', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='bnet.protocol.channel.ChannelState.name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delegate_name', full_name='bnet.protocol.channel.ChannelState.delegate_name', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel_type', full_name='bnet.protocol.channel.ChannelState.channel_type', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("default").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='program', full_name='bnet.protocol.channel.ChannelState.program', index=10,
      number=11, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allow_offline_members', full_name='bnet.protocol.channel.ChannelState.allow_offline_members', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subscribe_to_presence', full_name='bnet.protocol.channel.ChannelState.subscribe_to_presence', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='bnet.protocol.channel.ChannelState.channel', index=13,
      number=100, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='presence', full_name='bnet.protocol.channel.ChannelState.presence', index=14,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHANNELSTATE_PRIVACYLEVEL,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=732,
  serialized_end=1456,
)


_MEMBERSTATE = _descriptor.Descriptor(
  name='MemberState',
  full_name='bnet.protocol.channel.MemberState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.channel.MemberState.attribute', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role', full_name='bnet.protocol.channel.MemberState.role', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='privileges', full_name='bnet.protocol.channel.MemberState.privileges', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='bnet.protocol.channel.MemberState.info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hidden', full_name='bnet.protocol.channel.MemberState.hidden', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1459,
  serialized_end=1633,
)


_MEMBER = _descriptor.Descriptor(
  name='Member',
  full_name='bnet.protocol.channel.Member',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identity', full_name='bnet.protocol.channel.Member.identity', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='bnet.protocol.channel.Member.state', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1635,
  serialized_end=1737,
)

_MESSAGE.fields_by_name['attribute'].message_type = bnet.attribute_pb2._ATTRIBUTE
_FINDCHANNELOPTIONS.fields_by_name['attribute_filter'].message_type = bnet.attribute_pb2._ATTRIBUTEFILTER
_CHANNELDESCRIPTION.fields_by_name['channel_id'].message_type = bnet.entity_pb2._ENTITYID
_CHANNELDESCRIPTION.fields_by_name['state'].message_type = _CHANNELSTATE
_CHANNELINFO.fields_by_name['description'].message_type = _CHANNELDESCRIPTION
_CHANNELINFO.fields_by_name['member'].message_type = _MEMBER
_CHANNELSTATE.fields_by_name['attribute'].message_type = bnet.attribute_pb2._ATTRIBUTE
_CHANNELSTATE.fields_by_name['invitation'].message_type = bnet.invitation_types_pb2._INVITATION
_CHANNELSTATE.fields_by_name['privacy_level'].enum_type = _CHANNELSTATE_PRIVACYLEVEL
_CHANNELSTATE.fields_by_name['channel'].message_type = _CHANNELSTATE
_CHANNELSTATE.fields_by_name['presence'].message_type = bnet.presence_types_pb2._CHANNELSTATE
_CHANNELSTATE_PRIVACYLEVEL.containing_type = _CHANNELSTATE
_MEMBERSTATE.fields_by_name['attribute'].message_type = bnet.attribute_pb2._ATTRIBUTE
_MEMBERSTATE.fields_by_name['info'].message_type = bnet.entity_pb2._ACCOUNTINFO
_MEMBER.fields_by_name['identity'].message_type = bnet.entity_pb2._IDENTITY
_MEMBER.fields_by_name['state'].message_type = _MEMBERSTATE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['FindChannelOptions'] = _FINDCHANNELOPTIONS
DESCRIPTOR.message_types_by_name['ChannelDescription'] = _CHANNELDESCRIPTION
DESCRIPTOR.message_types_by_name['ChannelInfo'] = _CHANNELINFO
DESCRIPTOR.message_types_by_name['ChannelState'] = _CHANNELSTATE
DESCRIPTOR.message_types_by_name['MemberState'] = _MEMBERSTATE
DESCRIPTOR.message_types_by_name['Member'] = _MEMBER

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'bnet.channel_types_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.Message)
  ))
_sym_db.RegisterMessage(Message)

FindChannelOptions = _reflection.GeneratedProtocolMessageType('FindChannelOptions', (_message.Message,), dict(
  DESCRIPTOR = _FINDCHANNELOPTIONS,
  __module__ = 'bnet.channel_types_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.FindChannelOptions)
  ))
_sym_db.RegisterMessage(FindChannelOptions)

ChannelDescription = _reflection.GeneratedProtocolMessageType('ChannelDescription', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELDESCRIPTION,
  __module__ = 'bnet.channel_types_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.ChannelDescription)
  ))
_sym_db.RegisterMessage(ChannelDescription)

ChannelInfo = _reflection.GeneratedProtocolMessageType('ChannelInfo', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELINFO,
  __module__ = 'bnet.channel_types_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.ChannelInfo)
  ))
_sym_db.RegisterMessage(ChannelInfo)

ChannelState = _reflection.GeneratedProtocolMessageType('ChannelState', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELSTATE,
  __module__ = 'bnet.channel_types_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.ChannelState)
  ))
_sym_db.RegisterMessage(ChannelState)

MemberState = _reflection.GeneratedProtocolMessageType('MemberState', (_message.Message,), dict(
  DESCRIPTOR = _MEMBERSTATE,
  __module__ = 'bnet.channel_types_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.MemberState)
  ))
_sym_db.RegisterMessage(MemberState)

Member = _reflection.GeneratedProtocolMessageType('Member', (_message.Message,), dict(
  DESCRIPTOR = _MEMBER,
  __module__ = 'bnet.channel_types_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.channel.Member)
  ))
_sym_db.RegisterMessage(Member)


_MEMBERSTATE.fields_by_name['role'].has_options = True
_MEMBERSTATE.fields_by_name['role']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
