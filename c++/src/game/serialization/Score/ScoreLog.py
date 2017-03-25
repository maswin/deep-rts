# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Score

import flatbuffers

class ScoreLog(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsScoreLog(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ScoreLog()
        x.Init(buf, n + offset)
        return x

    # ScoreLog
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ScoreLog
    def GameNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # ScoreLog
    def Items(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .ScorePlayer import ScorePlayer
            obj = ScorePlayer()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ScoreLog
    def ItemsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ScoreLogStart(builder): builder.StartObject(2)
def ScoreLogAddGameNum(builder, gameNum): builder.PrependUint32Slot(0, gameNum, 0)
def ScoreLogAddItems(builder, items): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(items), 0)
def ScoreLogStartItemsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ScoreLogEnd(builder): return builder.EndObject()
