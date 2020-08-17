# Drag-and-Drop-Importer-for-SideFx-Houdini
Drag and Drop Importer for houdini (many functions still need to improved)拖曳导入文件的窗口，很多功能都还没整，感觉也没时间整的样子((


作者:AWACS 时间:2020.08.17

## 安装方法 
### 可以直接看gif的,直接跳过
- 在工具架上添加这行代码 ：  
import sys  
sys.path.append( "#your path of script file" )  
import DragDropImporter  
reload (DragDropImporter)  
- 例如我的脚本文件的路径是：D:/1T/HOUPY/tempppp/DragDropImporter.py
那么就是：  
import sys  
sys.path.append("D:/1T/HOUPY/tempppp")  
import DragDropImporter  
reload (DragDropImporter)  


-----------------------------

## How to install:
### You can just skip this ,just reference to that gif file
- Add this to your shelf:  
import sys  
sys.path.append( "#your path of script file" )  
import DragDropImporter  
reload (DragDropImporter)  
- Example ,my path of script is ：D:/1T/HOUPY/tempppp/DragDropImporter.py  
import sys  
sys.path.append("D:/1T/HOUPY/tempppp")  
import DragDropImporter  
reload (DragDropImporter)  

## 其他：
- 目前也就导个obj比较好用吧,然鹅连个材质导入都还没整，其他的以后整(
- transform节点的属性设置的窗口里是支持直接输入表达式的
- 很多其他格式的文件的导入都还没开始考虑，不同的读取节点，还有帧数问题等等，都还没加，目前别的只可以直接强行拖进去用file节点读
- Fbx目前莫得导入设置，目前只是和默认导入的默认设置一样
- 以后可能加个自定义导入后接什么节点的功能
- 话说感觉也没时间精力整这破玩意，写的乱七八糟，溜了溜了

## Others：
- Only a little useful when batch obj files for now/.......whatever
- You can stright type expression in transform Node attribute setting window 
- No considering for other format,material,read file node,frame rate,etcetc, still improving
- Fbx format has no import setting yet , only equivalent to the default setting of import panel
- May be add a function for customize what node to add after import
- may be NO much time for doing this shxx,sorry
