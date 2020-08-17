# Drag-and-Drop-Importer-for-SideFx-Houdini
Drag and Drop Importer for houdini (many functions still need to improved)拖曳导入文件的窗口，很多功能都还没整，感觉也没时间整的样子((

作者:AWACS 时间:2020.08.17

### 安装方法 
## 可以直接看gif的,直接跳过
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

### How to install:
## You can just skip this ,just reference to that gif file
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

### 其他：
- transform节点的属性设置的窗口里是支持直接输入表达式的
- 以后可能加个自定义导入后接什么节点的功能
- 话说感觉也没时间精力整这破玩意，写的乱七八糟溜了溜了

### Others：
- You can stright type expression in transform Node attribute setting window 
- May be add a function for customize what node to add after import
- may be much time for doing this shxx,sorry
