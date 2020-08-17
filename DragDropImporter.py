# -!- coding: utf-8 -!-
# Author  : AWACS
# Time    : 2020/08/17
# version : 0.52 beta 

version = "0.52 ( beta )"

import hou
import os
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class Setting_Panel_Main(QWidget):
    def __init__( self, parent ):
        super(Setting_Panel_Main, self).__init__(parent)
        # self.Width = 400
        # self.Height = 30
        # self.setFixedSize( self.Width, self.Height )
        self.main_layout = QVBoxLayout()
        self.main_layout_empty = QHBoxLayout()
        self.main_layout_Btn = QHBoxLayout()

        self.TF_Attr_panel = QVBoxLayout( )


        self.main_layout.setSpacing(4)
        self.main_layout.setContentsMargins(1, 4, 1, 4)
        self.setLayout(self.main_layout)
        self.main_layout.addLayout(self.main_layout_empty)
        self.main_layout.addLayout(self.TF_Attr_panel)

        self.Spacer = QSpacerItem(150, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_layout_empty.addSpacerItem(self.Spacer)

        # self.TextCBMerge = QLabel (  )
        self.CB_Add_transform = QCheckBox( "Add transform node for each import file" )

        self.CB_Add_merge = QCheckBox( "Add a merge node at the end if import multiple files" )



        self.TF_Translate = QHBoxLayout()
        self.TF_TLABEL = QLabel(' Translate' )
        self.TF_TLABEL.setFixedSize ( 70 , 20)
        self.TF_TX = QLineEdit('')
        self.TF_TY = QLineEdit('')
        self.TF_TZ = QLineEdit('')
        self.TF_TX.setText( "0")
        self.TF_TY.setText( "0")
        self.TF_TZ.setText( "0")
        self.TF_Translate.addWidget(self.TF_TLABEL)
        self.TF_Translate.addWidget(self.TF_TX)
        self.TF_Translate.addWidget(self.TF_TY)
        self.TF_Translate.addWidget(self.TF_TZ)

        self.TF_Rotate = QHBoxLayout()
        self.TF_RLABEL = QLabel(' Rotate')
        self.TF_RLABEL.setFixedSize ( 70 , 20)
        self.TF_RX = QLineEdit('')
        self.TF_RY = QLineEdit('')
        self.TF_RZ = QLineEdit('')
        self.TF_RX.setText( "0")
        self.TF_RY.setText( "0")
        self.TF_RZ.setText( "0")
        self.TF_Rotate.addWidget(self.TF_RLABEL)
        self.TF_Rotate.addWidget(self.TF_RX)
        self.TF_Rotate.addWidget(self.TF_RY)
        self.TF_Rotate.addWidget(self.TF_RZ)

        self.TF_Scale = QHBoxLayout()
        self.TF_SLABEL = QLabel(' Scale')
        self.TF_SLABEL.setFixedSize ( 70 , 20)
        self.TF_SX = QLineEdit('')
        self.TF_SY = QLineEdit('')
        self.TF_SZ = QLineEdit('')
        self.TF_SX.setText( "1")
        self.TF_SY.setText( "1")
        self.TF_SZ.setText( "1")
        self.TF_Scale.addWidget(self.TF_SLABEL)
        self.TF_Scale.addWidget(self.TF_SX)
        self.TF_Scale.addWidget(self.TF_SY)
        self.TF_Scale.addWidget(self.TF_SZ)

        self.TF_U_Scale = QHBoxLayout()
        self.TF_UniformScale_Label = QLabel(' Uniform Scale')
        self.TF_UniformScale  = QLineEdit('')
        self.TF_UniformScale.setText( "1" )
        self.TF_U_Scale.addWidget( self.TF_UniformScale_Label )
        self.TF_U_Scale.addWidget( self.TF_UniformScale )




        self.TF_Attr_panel.addWidget(self.CB_Add_transform)
        self.TF_Attr_panel.addWidget(self.CB_Add_merge)

        self.TF_Attr_panel_Label = QLabel ( " Transform Attribute (Expression Supported) :" )
        self.TF_Attr_panel.addWidget( self.TF_Attr_panel_Label )

        self.TF_Attr_panel.addLayout( self.TF_Translate )
        self.TF_Attr_panel.addLayout( self.TF_Rotate )
        self.TF_Attr_panel.addLayout( self.TF_Scale )
        self.TF_Attr_panel.addLayout( self.TF_U_Scale )




"""
#不妥我没时间没整好这个不玩了。。。。。
class FbxSettingPanel(QWidget):
    def __init__( self, parent = None ):
        super( FbxSettingPanel , self).__init__(parent)

        self.Width = 390
        self.Height = 50
        self.setFixedSize( self.Width, self.Height )
        # self.setFocusPolicy( Qt.ClickFocus )
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing( 4 )
        self.main_layout.setContentsMargins(1,1,1,1)

        self.setLayout(self.main_layout)
        self.Button_Set = QPushButton('RUA Window')
        self.main_layout.addWidget( self.Button_Set )

"""

class DragDropImporter(QWidget):
    def __init__( self, parent = None ):
        super(DragDropImporter, self).__init__(parent)
        self.setWindowTitle( u'Drag & Drop Importer 拖曳导入窗口 ' + version +' By_@AWACS')
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setMinimumWidth(640)
        self.setMinimumHeight(400)
        mainlayout = QVBoxLayout()
        mainlayout.setContentsMargins(1, 1, 1, 1)
        self.settingPanel = Setting_Panel_Main(self)
        # self.FbxSettingPanel = FbxSettingPanel(self)

        self.setLayout(mainlayout)
        mainlayout.addWidget(self.settingPanel)
        # mainlayout.addWidget(self.FbxSettingPanel)
        self.setAcceptDrops(True)
        self.text = None

        self.File_List = []
        self.File_List_Final = []



    def Get_transform_Attr( self ):
        QtAttrlist = [ "TX" ,"TY" ,"TZ" ,
                     "RX" ,"RY" ,"RZ" ,
                     "SX" ,"SY" ,"SZ" ,
                        "UniformScale"]
        return_list = []
        # print ( eval("self.settingPanel.main_layout") )
        for indlineedit in QtAttrlist:
             return_list.append ( eval("self.settingPanel.TF_" + indlineedit +".text()") )
        # print "======================="
        # help( self.settingPanel.CB_Add_transform )

        # print return_list
        return return_list

    def dragEnterEvent( self, event ):
        self.text = event.mimeData().text()

        self.File_List = (self.text.split("file:///"))

    def dropEvent( self, event ):
        # print("aaaa" + str(len(self.File_List)))
        # print("aaaa" + str(self.File_List))
        for indfile in self.File_List:
            ind = indfile.replace("\n", "")
            # print("--------------")
            # print (ind)
            # print (type(ind))
            # print (os.path.isfile(str(ind)))
            # print (os.path.isfile(ind))
            if os.path.isfile(ind):

                ext = os.path.splitext(str(ind))[1]
                # print (ext)
                if ext.lower() in ['.obj', '.fbx', '.vdb']:
                    self.File_List_Final.append(str(ind))
        # print(self.File_List_Final)
        self.import_Object()

    def paintEvent( self, event ):
        p = QPainter()
        p.begin(self)
        p.setPen(Qt.NoPen)
        p.setBrush(QBrush( QColor ( 50 , 50 , 50 )))
        p.drawRect(self.rect())

        font = QFont()
        font.setPixelSize(18)
        font.setFamily("微软雅黑")

        p.setFont(font)

        p.setPen(QPen(QColor(200, 200, 200)))
        p.setBrush(Qt.NoBrush)
        p.drawText(self.rect(), Qt.AlignHCenter,
                   '1. Select a Geometry Node or No selection at all\n' \
                   '2.Drag And Drop The File Into This Window\n' \
                   '3.Supported Format (Currently) : Obj Fbx Vdb \n' \
                   '4.Fbx format has no import setting yet , \n' \
                   'only equivalent to the default setting of import panel : \n' \
                   '5.This tool is just started recently,many functions is still improving, \n'  \
                   'there might be some issue if import other format \n' 
                   )
        p.end()

    def get_selection_import_to( self ):
        try:
            path = str(hou.selectedNodes()[0].type().name())
        except:
            path = False
        if path == "geo":
            return hou.selectedNodes()[0].path()
        else:
            return False

    def import_Object( self ):
        Add_merge = self.settingPanel.CB_Add_merge.isChecked()
        Add_transform = self.settingPanel.CB_Add_transform.isChecked()

        print("Importing " + str(len(self.File_List_Final)) + " Files")
        import_to_path = self.get_selection_import_to()
        if import_to_path == False:
            ext = os.path.splitext( self.File_List_Final[0] )[1]
            if ext.lower() == ".fbx":
                self.FBX_import(import_to_path, single_file)

            print("Invaild import path ,Please select a Geometry type Node")
        else:
            Result = []
            for single_file in self.File_List_Final:
                ext = os.path.splitext(single_file)[1]
                # print (ext)
                # print (import_to_path)
                if ext.lower() == ".obj":
                    Result.append(self.OBJ_import(import_to_path, single_file , Add_transform) [-1])

                elif ext.lower() == ".vdb":
                    Result.append(self.OBJ_import(import_to_path, single_file , Add_transform) [-1])

                elif ext.lower() == ".fbx":
                    self.FBX_import(import_to_path, single_file)
                else:
                    try:
                        Result.append(self.OBJ_import(import_to_path, single_file , Add_transform) [-1])
                    except:
                        print("may have some issue while import this file : " + single_file )

            if ext.lower() != ".fbx":
                if Add_merge:
                    self.Merge_All( import_to_path , Result )

        self.File_List = []
        self.File_List_Final = []

    def OBJ_import( self, Path, File , Add_transform):
        file_node = hou.node(Path).createNode("file")
        file_node.parm("file").set(File)
        if Add_transform:
            Xform_node = self.add_Transfrom_node_and_setattr ( Path , file_node )
            return [ file_node , Xform_node ]
        else: 
            return [ file_node ]
    def add_Transfrom_node_and_setattr( self , Path , input_Node  ):
        Xform_node = hou.node(Path).createNode("xform")

        Attrlist = self.Get_transform_Attr()
        Attrnamelist = [ "tx" ,"ty" ,"tz" ,
                     "rx" ,"ry" ,"rz" ,
                     "sx" ,"sy" ,"sz" ,
                     "scale" ]
        for indAttr_index in range(len(Attrnamelist)):
            if len(Attrlist [ indAttr_index ]) == 0 :
                continue
            try:
                Xform_node.parm( Attrnamelist[indAttr_index] ).set( Attrlist [ indAttr_index ])
            except:
                Xform_node.parm( Attrnamelist[indAttr_index] ).setExpression( Attrlist [ indAttr_index ])

        Xform_node.setFirstInput(input_Node)
        return Xform_node


    def Merge_All( self , Path,  Nodelist ):
        Xform_node = hou.node(Path).createNode("merge")
        for indnodeindex in range(len(Nodelist)):
            Xform_node.setNextInput( Nodelist[indnodeindex] )


    def FBX_import( self, Path, File ):

        hou.hipFile.importFBX(File,
                              suppress_save_prompt = False,
                              merge_into_scene = True,
                              import_cameras = True,
                              import_joints_and_skin = True,
                              import_geometry = True,
                              import_lights = True,
                              import_animation = True,
                              import_materials = True,
                              resample_animation = False,
                              resample_interval = 1.0,
                              override_framerate = False,
                              framerate = -1,
                              hide_joints_attached_to_skin = True,
                              convert_joints_to_zyx_rotation_order = False,
                              material_mode = hou.fbxMaterialMode.FBXShaderNodes,
                              compatibility_mode = hou.fbxCompatibilityMode.Maya,
                              single_precision_vertex_caches = False,
                              triangulate_nurbs = False,
                              triangulate_patches = False,
                              import_global_ambient_light = False,
                              import_blend_deformers_as_blend_sops = False,
                              segment_scale_already_baked_in = True,
                              convert_file_paths_to_relative = True,
                              unlock_geometry = False,
                              unlock_deformations = False,
                              import_nulls_as_subnets = False,
                              import_into_object_subnet = True,
                              convert_into_y_up_coordinate_system = False)


def DragDropImporter_dialog_show():
    DragDropImporter_dialog = DragDropImporter()
    DragDropImporter_dialog.setParent(hou.qt.floatingPanelWindow(None), Qt.Window)
    DragDropImporter_dialog.show()



DragDropImporter_dialog_show()