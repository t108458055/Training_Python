# install  kit ,that commit "py -m pip install occ"
import math
from OCC.Core.gp import (gp_Pnt, gp_OX, gp_Vec, gp_Trsf, gp_DZ, gp_Ax2, gp_Ax3, gp_Pnt2d, gp_Dir2d, gp_Ax2d, gp_Pln)
from OCC.Core.GC import GC_MakeArcOfCircle, GC_MakeSegment
from OCC.Core.GCE2d import GCE2d_MakeSegment
from OCC.Core.Geom import Geom_CylindricalSurface
from OCC.Core.Geom2d import Geom2d_Ellipse, Geom2d_TrimmedCurve
from OCC.Core.BRepBuilderAPI import (BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace, BRepBuilderAPI_Transform)
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism, BRepPrimAPI_MakeCylinder
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeFillet
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.BRepOffsetAPI import BRepOffsetAPI_MakeThickSolid, BRepOffsetAPI_ThruSections
from OCC.Core.BRepLib import breplib
from OCC.Core.BRep import BRep_Builder
from OCC.Core.GeomAbs import GeomAbs_Plane
from OCC.Core.BRepAdaptor import BRepAdaptor_Surface
from OCC.Core.TopoDS import topods, TopoDS_Compound, TopoDS_Face
from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopAbs import TopAbs_EDGE, TopAbs_FACE
from OCC.Core.TopTools import TopTools_ListOfShape

# 高度= 70，寬度= 50，厚度= 30
height = 70
width = 50
thickness = 30

# 將用來創建瓶身輪廓的點
aPnt1 = gp_Pnt(-width / 2.0, 0, 0)
aPnt2 = gp_Pnt(-width / 2.0, -thickness / 4.0, 0)
aPnt3 = gp_Pnt(0, -thickness / 2.0, 0)
aPnt4 = gp_Pnt(width / 2.0, -thickness / 4.0, 0)
aPnt5 = gp_Pnt(width / 2.0, 0, 0)

aArcOfCircle = GC_MakeArcOfCircle(aPnt2, aPnt3, aPnt4)
aSegment1 = GC_MakeSegment(aPnt1, aPnt2) #段1
aSegment2 = GC_MakeSegment(aPnt4, aPnt5)#段2

# 也可以直接使用點而不是結果線來構造線邊緣
aEdge1 = BRepBuilderAPI_MakeEdge(aSegment1.Value())
aEdge2 = BRepBuilderAPI_MakeEdge(aArcOfCircle.Value())
aEdge3 = BRepBuilderAPI_MakeEdge(aSegment2.Value())

# 從邊緣創建導線
aWire = BRepBuilderAPI_MakeWire(aEdge1.Edge(), aEdge2.Edge(), aEdge3.Edge())

# 快速指定 X 軸
xAxis = gp_OX()

# 設置鏡像
aTrsf = gp_Trsf()
aTrsf.SetMirror(xAxis)

# 應用鏡像變換
aBRespTrsf = BRepBuilderAPI_Transform(aWire.Wire(), aTrsf)

# 從變換中取出鏡像形狀並轉換回線
aMirroredShape = aBRespTrsf.Shape()

# 現在是導線而不是普通形狀
aMirroredWire = topods.Wire(aMirroredShape)

# 將兩個組成導線合併
mkWire = BRepBuilderAPI_MakeWire()
mkWire.Add(aWire.Wire())
mkWire.Add(aMirroredWire)
myWireProfile = mkWire.Wire()

# 我們將扫過的脸做成棱镜
myFaceProfile = BRepBuilderAPI_MakeFace(myWireProfile)

# 我們希望沿著Z軸將面扫至高度
aPrismVec = gp_Vec(0, 0, height)
myBody_step1 = BRepPrimAPI_MakePrism(myFaceProfile.Face(), aPrismVec)

# 向所有邊添加圓角
mkFillet = BRepFilletAPI_MakeFillet(myBody_step1.Shape())
anEdgeExplorer = TopExp_Explorer(myBody_step1.Shape(), TopAbs_EDGE)

while anEdgeExplorer.More():
    anEdge = topods.Edge(anEdgeExplorer.Current())
    mkFillet.Add(thickness / 12.0, anEdge)
    anEdgeExplorer.Next()

# 創造瓶頸
neckLocation = gp_Pnt(0, 0, height)
neckAxis = gp_DZ()
neckAx2 = gp_Ax2(neckLocation, neckAxis)
myNeckRadius = thickness / 4.0
myNeckHeight = height / 10.0
mkCylinder = BRepPrimAPI_MakeCylinder(neckAx2, myNeckRadius, myNeckHeight)

myBody_step2 = BRepAlgoAPI_Fuse(mkFillet.Shape(), mkCylinder.Shape())
