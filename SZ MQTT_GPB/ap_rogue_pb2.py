# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ap_rogue.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ap_rogue.proto',
  package='',
  syntax='proto2',
  serialized_options=_b('\n\037com.ruckuswireless.scg.protobuf'),
  serialized_pb=_b('\n\x0e\x61p_rogue.proto\"\xf3\x02\n\nReportType\x12\x10\n\x08rogueMac\x18\x01 \x01(\t\x12\x0c\n\x04rssi\x18\x02 \x01(\r\x12\x12\n\nencryption\x18\x03 \x01(\t\x12\r\n\x05radio\x18\x04 \x01(\t\x12\x0f\n\x07\x63hannel\x18\x05 \x01(\r\x12\x11\n\ttimeStamp\x18\x06 \x01(\x04\x12\x0c\n\x04ssid\x18\x07 \x01(\t\x12\x0e\n\x06wlanId\x18\x08 \x01(\x05\x12\x12\n\nrogueAPMac\x18\t \x01(\t\x12\x13\n\x0bisSendEvent\x18\n \x01(\x05\x12\x0c\n\x04type\x18\x0b \x01(\t\x12\x19\n\x11prevReportChannel\x18\x0c \x01(\r\x12\x16\n\x0eprevReportType\x18\r \x01(\t\x12(\n\trogueType\x18\x0e \x01(\x0e\x32\x15.ReportType.RogueType\x12\x15\n\rrogueTypeInfo\x18\x0f \x01(\r\"5\n\tRogueType\x12\r\n\tDISCOVERY\x10\x00\x12\n\n\x06UPDATE\x10\x01\x12\r\n\tDISAPPEAR\x10\x02\"\xdd\x03\n\x0cRogueAPStats\x12\x0f\n\x07version\x18\x01 \x02(\r\x12\r\n\x05\x61pMac\x18\x02 \x01(\t\x12\x0e\n\x06\x61pName\x18\x03 \x01(\t\x12\x0f\n\x07zone_id\x18\x04 \x01(\t\x12\x0f\n\x07protect\x18\x05 \x01(\t\x12\"\n\rapRogueUpdate\x18\x06 \x03(\x0b\x32\x0b.ReportType\x12\x12\n\napgroup_id\x18\x07 \x01(\t\x12\x12\n\ncluster_id\x18\x08 \x01(\t\x12\x11\n\tdomain_id\x18\t \x01(\t\x12\x13\n\x0b\x61ptenant_id\x18\n \x01(\t\x12\x0e\n\x06map_id\x18\x0b \x01(\t\x12\x15\n\raptenant_name\x18\x0c \x01(\t\x12\x11\n\tzone_name\x18\r \x01(\t\x12\x14\n\x0c\x61pgroup_name\x18\x0e \x01(\t\x12\x13\n\x0b\x64omain_name\x18\x0f \x01(\t\x12\x1d\n\x15\x63ontrollerShouldFlush\x18\x10 \x01(\x05\x12\x12\n\nsampleTime\x18\x11 \x01(\x04\x12\x1b\n\x13\x61ggregationInterval\x18\x12 \x01(\r\x12\x11\n\ttimestamp\x18\x13 \x01(\x04\x12\x16\n\x0eoperation_type\x18\x14 \x01(\r\x12\x12\n\ntotPpduDur\x18\x15 \x01(\x04\x12\x13\n\x0btotScanTime\x18\x16 \x01(\x04\x42!\n\x1f\x63om.ruckuswireless.scg.protobuf')
)



_REPORTTYPE_ROGUETYPE = _descriptor.EnumDescriptor(
  name='RogueType',
  full_name='ReportType.RogueType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DISCOVERY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISAPPEAR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=337,
  serialized_end=390,
)
_sym_db.RegisterEnumDescriptor(_REPORTTYPE_ROGUETYPE)


_REPORTTYPE = _descriptor.Descriptor(
  name='ReportType',
  full_name='ReportType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rogueMac', full_name='ReportType.rogueMac', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='ReportType.rssi', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encryption', full_name='ReportType.encryption', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radio', full_name='ReportType.radio', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='ReportType.channel', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='ReportType.timeStamp', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ssid', full_name='ReportType.ssid', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wlanId', full_name='ReportType.wlanId', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rogueAPMac', full_name='ReportType.rogueAPMac', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isSendEvent', full_name='ReportType.isSendEvent', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='ReportType.type', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prevReportChannel', full_name='ReportType.prevReportChannel', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prevReportType', full_name='ReportType.prevReportType', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rogueType', full_name='ReportType.rogueType', index=13,
      number=14, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rogueTypeInfo', full_name='ReportType.rogueTypeInfo', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REPORTTYPE_ROGUETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=390,
)


_ROGUEAPSTATS = _descriptor.Descriptor(
  name='RogueAPStats',
  full_name='RogueAPStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='RogueAPStats.version', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apMac', full_name='RogueAPStats.apMac', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apName', full_name='RogueAPStats.apName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zone_id', full_name='RogueAPStats.zone_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protect', full_name='RogueAPStats.protect', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apRogueUpdate', full_name='RogueAPStats.apRogueUpdate', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apgroup_id', full_name='RogueAPStats.apgroup_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='RogueAPStats.cluster_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='RogueAPStats.domain_id', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aptenant_id', full_name='RogueAPStats.aptenant_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_id', full_name='RogueAPStats.map_id', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aptenant_name', full_name='RogueAPStats.aptenant_name', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zone_name', full_name='RogueAPStats.zone_name', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apgroup_name', full_name='RogueAPStats.apgroup_name', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_name', full_name='RogueAPStats.domain_name', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='controllerShouldFlush', full_name='RogueAPStats.controllerShouldFlush', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sampleTime', full_name='RogueAPStats.sampleTime', index=16,
      number=17, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aggregationInterval', full_name='RogueAPStats.aggregationInterval', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='RogueAPStats.timestamp', index=18,
      number=19, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation_type', full_name='RogueAPStats.operation_type', index=19,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totPpduDur', full_name='RogueAPStats.totPpduDur', index=20,
      number=21, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totScanTime', full_name='RogueAPStats.totScanTime', index=21,
      number=22, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=393,
  serialized_end=870,
)

_REPORTTYPE.fields_by_name['rogueType'].enum_type = _REPORTTYPE_ROGUETYPE
_REPORTTYPE_ROGUETYPE.containing_type = _REPORTTYPE
_ROGUEAPSTATS.fields_by_name['apRogueUpdate'].message_type = _REPORTTYPE
DESCRIPTOR.message_types_by_name['ReportType'] = _REPORTTYPE
DESCRIPTOR.message_types_by_name['RogueAPStats'] = _ROGUEAPSTATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReportType = _reflection.GeneratedProtocolMessageType('ReportType', (_message.Message,), {
  'DESCRIPTOR' : _REPORTTYPE,
  '__module__' : 'ap_rogue_pb2'
  # @@protoc_insertion_point(class_scope:ReportType)
  })
_sym_db.RegisterMessage(ReportType)

RogueAPStats = _reflection.GeneratedProtocolMessageType('RogueAPStats', (_message.Message,), {
  'DESCRIPTOR' : _ROGUEAPSTATS,
  '__module__' : 'ap_rogue_pb2'
  # @@protoc_insertion_point(class_scope:RogueAPStats)
  })
_sym_db.RegisterMessage(RogueAPStats)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
