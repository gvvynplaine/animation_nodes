import bpy
from .. utils.nodes import getAnimationNodeTrees

def drawMenu(self, context):
    if context.space_data.tree_type != "an_AnimationNodeTree": return

    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"

    drawNodeTreeChooser(layout, context)

    layout.operator("an.insert_node", text = "Search", icon = "VIEWZOOM")
    layout.separator()
    layout.menu("an.number_menu", text = "Number")
    layout.menu("an.vector_menu", text = "Vector")
    layout.menu("an.matrix_menu", text = "Matrix")
    layout.menu("an.text_menu", text = "Text")
    layout.menu("an.boolean_menu", text = "Boolean")
    layout.menu("an.color_menu", text = "Color")
    layout.menu("an.list_menu", text = "List")
    layout.separator()
    layout.menu("an.object_menu", text = "Object")
    layout.menu("an.mesh_menu", text = "Mesh")
    layout.menu("an.spline_menu", text = "Spline")
    layout.separator()
    layout.menu("an.sound_menu", text = "Sound")
    layout.menu("an.material_menu", text = "Material")
    layout.menu("an.animation_menu", text = "Animation")
    layout.menu("an.particles_menu", text = "Particles")
    layout.separator()
    layout.menu("an.system_menu", text = "System")

def drawNodeTreeChooser(layout, context):
    activeNodeTree = context.space_data.node_tree
    nodeTrees = getAnimationNodeTrees()

    if not activeNodeTree:
        col = layout.column()
        col.scale_y = 1.6
        if len(nodeTrees) == 0:
            col.operator("an.create_node_tree", text = "New Node Tree", icon = "PLUS")
        else:
            for nodeTree in nodeTrees:
                props = col.operator("an.select_node_tree", text = "Select '{}'".format(nodeTree.name), icon = "EYEDROPPER")
                props.nodeTreeName = nodeTree.name


class NumberMenu(bpy.types.Menu):
    bl_idname = "an.number_menu"
    bl_label = "Number Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_DataInputNode", "Integer", {"assignedType" : repr("Integer")})
        insertNode(layout, "an_DataInputNode", "Float", {"assignedType" : repr("Float")})
        insertNode(layout, "an_CreateListNode", "Integer List", {"assignedType" : repr("Integer")})
        insertNode(layout, "an_CreateListNode", "Float List", {"assignedType" : repr("Float")})
        insertNode(layout, "an_FloatRangeListNode", "Range")
        layout.separator()
        insertNode(layout, "an_RandomNumberNode", "Randomize")
        insertNode(layout, "an_FloatWiggleNode", "Wiggle")
        insertNode(layout, "an_BlendDataNode", "Blend", {"dataType" : repr("Float")})
        layout.separator()
        insertNode(layout, "an_FloatClampNode", "Clamp")
        insertNode(layout, "an_ConvertAngleNode", "Convert Angle")
        insertNode(layout, "an_FloatMathNode", "Math")

class VectorMenu(bpy.types.Menu):
    bl_idname = "an.vector_menu"
    bl_label = "Vector Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_SeparateVectorNode", "Separate")
        insertNode(layout, "an_CombineVectorNode", "Combine")
        insertNode(layout, "an_VectorFromValueNode", "From Value")
        insertNode(layout, "an_CreateListNode", "List", {"assignedType" : repr("Vector")})
        layout.separator()
        insertNode(layout, "an_RandomVectorNode", "Randomize")
        insertNode(layout, "an_VectorWiggleNode", "Wiggle")
        insertNode(layout, "an_BlendDataNode", "Blend", {"dataType" : repr("Vector")})
        layout.separator()
        insertNode(layout, "an_VectorLengthNode", "Length")
        insertNode(layout, "an_VectorDistanceNode", "Distance")
        insertNode(layout, "an_VectorMathNode", "Math")
        insertNode(layout, "an_DirectionToRotationNode", "Direction to Rotation")
        insertNode(layout, "an_TransformVectorNode", "Transform")

class MatrixMenu(bpy.types.Menu):
    bl_idname = "an.matrix_menu"
    bl_label = "Matrix Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_DecomposeMatrixNode", "Decompose")
        insertNode(layout, "an_ComposeMatrixNode", "Compose")
        insertNode(layout, "an_CreateListNode", "List", {"assignedType" : repr("Matrix")})
        layout.separator()
        insertNode(layout, "an_TranslationMatrixNode", "Translation")
        insertNode(layout, "an_RotationMatrixNode", "Rotation")
        insertNode(layout, "an_ScaleMatrixNode", "Scale")
        insertNode(layout, "an_MatrixCombineNode", "Combine")
        layout.separator()
        insertNode(layout, "an_BlendDataNode", "Blend", {"dataType" : repr("Matrix")})
        insertNode(layout, "an_InvertMatrixNode", "Invert")
        insertNode(layout, "an_MatrixMathNode", "Math")

class TextMenu(bpy.types.Menu):
    bl_idname = "an.text_menu"
    bl_label = "Text Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_DataInputNode", "Input", {"assignedType" : repr("String")})
        insertNode(layout, "an_CreateListNode", "List", {"assignedType" : repr("String")})
        insertNode(layout, "an_RandomStringNode", "Randomize")
        insertNode(layout, "an_CharactersNode", "Characters")
        layout.separator()
        insertNode(layout, "an_SplitTextNode", "Split")
        insertNode(layout, "an_JoinStringsNode", "Join")
        layout.separator()
        insertNode(layout, "an_ReplicateStringsNode", "Replicate")
        insertNode(layout, "an_TrimTextNode", "Trim")
        insertNode(layout, "an_StringLengthNode", "Length")
        layout.separator()
        insertNode(layout, "an_SeparateTextObjectNode", "Object Separate")
        insertNode(layout, "an_TextBlockReaderNode", "Block Reader")
        insertNode(layout, "an_TextBlockWriterNode", "Block Writer")
        insertNode(layout, "an_TextSequenceOutputNode", "Sequence Output")
        insertNode(layout, "an_TextOutputNode", "Object Output")

class BooleanMenu(bpy.types.Menu):
    bl_idname = "an.boolean_menu"
    bl_label = "Boolean Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_DataInputNode", "Boolean", {"assignedType" : repr("Boolean")})
        insertNode(layout, "an_InvertNode", "Invert")
        insertNode(layout, "an_CompareNode", "Compare")
        insertNode(layout, "an_SwitchNode", "Switch")

class ColorMenu(bpy.types.Menu):
    bl_idname = "an.color_menu"
    bl_label = "Color Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_ColorInputNode", "RGB")
        insertNode(layout, "an_CombineColorNode", "Combine RGBA")
        insertNode(layout, "an_ColorMixNode", "Mix")
        insertNode(layout, "an_SetVertexColorNode", "Set Vertex Color")

class ListMenu(bpy.types.Menu):
    bl_idname = "an.list_menu"
    bl_label = "List Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_CreateListNode", "Create")
        insertNode(layout, "an_CombineListsNode", "Combine")
        insertNode(layout, "an_AppendListNode", "Append")
        layout.separator()
        insertNode(layout, "an_GetListElementNode", "Get Element")
        insertNode(layout, "an_GetListLengthNode", "Get Length")
        layout.separator()
        insertNode(layout, "an_ShuffleListNode", "Shuffle")
        insertNode(layout, "an_ReverseListNode", "Reverse")


class ObjectMenu(bpy.types.Menu):
    bl_idname = "an.object_menu"
    bl_label = "Object Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_DataInputNode", "Input", {"assignedType" : repr("Object")})
        insertNode(layout, "an_CreateListNode", "List", {"assignedType" : repr("Object")})
        insertNode(layout, "an_ObjectGroupInputNode", "Group Input")
        layout.separator()
        insertNode(layout, "an_ObjectTransformsInputNode", "Transforms Input")
        insertNode(layout, "an_ObjectTransformsOutputNode", "Transforms Output")
        insertNode(layout, "an_ObjectMatrixInputNode", "Matrix Input")
        insertNode(layout, "an_ObjectMatrixOutputNode", "Matrix Output")
        insertNode(layout, "an_ObjectAttributeInputNode", "Attribute Input")
        insertNode(layout, "an_ObjectAttributeOutputNode", "Attribute Output")
        layout.separator()
        insertNode(layout, "an_ObjectIDKeyNode", "ID Key")
        insertNode(layout, "an_CopyObjectDataNode", "Copy Data")
        layout.separator()
        insertNode(layout, "an_ObjectInstancerNode", "Instancer")

class MeshMenu(bpy.types.Menu):
    bl_idname = "an.mesh_menu"
    bl_label = "Mesh Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_ObjectMeshInfoNode", "Data Info")
        insertNode(layout, "an_SeparateMeshDataNode", "Separate")
        insertNode(layout, "an_CombineMeshDataNode", "Combine")
        insertNode(layout, "an_AppendToMeshDataNode", "Append")
        layout.menu("an.mesh_operators_menu", text = "Operators")
        layout.separator()
        insertNode(layout, "an_CreateMeshFromDataNode", "Create from Data")
        insertNode(layout, "an_SetMeshOnObjectNode", "Set on Object")
        layout.menu("an.mesh_finalizing_menu", text = "Tools")
        layout.separator()
        insertNode(layout, "an_VertexInfoNode", "Vertex Info")
        insertNode(layout, "an_PolygonInfoNode", "Polygon Info")
        insertNode(layout, "an_TransformVertexNode", "Transform Vertex")
        insertNode(layout, "an_TransformPolygonNode", "Transform Polygon")

class MeshOperatorsMenu(bpy.types.Menu):
    bl_idname = "an.mesh_operators_menu"
    bl_label = "Mesh Operators Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_FindCloseVerticesNode", "Find Close Vertices")
        insertNode(layout, "an_EdgesToPlanesNode", "Edges to Planes")

class MeshFinalizingMenu(bpy.types.Menu):
    bl_idname = "an.mesh_finalizing_menu"
    bl_label = "Mesh Finalizing Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_MeshRemoveDoublesNode", "Remove Doubles")
        insertNode(layout, "an_MeshRecalculateFaceNormalsNode", "Recalculate Normals")
        insertNode(layout, "an_MakeObjectSmoothNode", "Smooth Object")

class SplineMenu(bpy.types.Menu):
    bl_idname = "an.spline_menu"
    bl_label = "Spline Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_SplinesFromObjectNode", "Get from Object")
        insertNode(layout, "an_CreateSplineNode", "Create from Points")
        insertNode(layout, "an_CreateListNode", "List", {"assignedType" : repr("Spline")})
        insertNode(layout, "an_AppendPointToSplineNode", "Append Point")
        insertNode(layout, "an_SmoothBezierSplineNode", "Smooth Bezier")
        insertNode(layout, "an_MakeSplineCyclicNode", "Make Cyclic")
        insertNode(layout, "an_TrimSplineNode", "Trim")
        insertNode(layout, "an_TransformSplineNode", "Transform")
        insertNode(layout, "an_SetSplinesOnObjectNode", "Set on Object")
        layout.separator()
        insertNode(layout, "an_SplineInfoNode", "Info")
        insertNode(layout, "an_EvaluateSplineNode", "Evaluate")
        insertNode(layout, "an_ProjectOnSplineNode", "Project")
        insertNode(layout, "an_GetSplineLengthNode", "Get Length")
        insertNode(layout, "an_GetSplineSamplesNode", "Get Samples")
        layout.separator()
        insertNode(layout, "an_LoftSplinesNode", "Loft")
        insertNode(layout, "an_RevolveSplineNode", "Revolve")

class SoundMenu(bpy.types.Menu):
    bl_idname = "an.sound_menu"
    bl_label = "Sound Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_SequencerSoundInputNode", "Sequencer Sound Input")

class MaterialMenu(bpy.types.Menu):
    bl_idname = "an.material_menu"
    bl_label = "Material Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_CyclesMaterialOutputNode", "Cycles Material Output")
        insertNode(layout, "an_ViewportColorNode", "Viewport Color")

class AnimationMenu(bpy.types.Menu):
    bl_idname = "an.animation_menu"
    bl_label = "Animation Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_TimeInfoNode", "Time Info")
        insertNode(layout, "an_SetKeyframesNode", "Set Keyframes")
        layout.separator()
        insertNode(layout, "an_InterpolationNode", "Interpolation")
        insertNode(layout, "an_EvaluateInterpolationNode", "Evaluate Interpolation")
        insertNode(layout, "an_MixInterpolationNode", "Mix Interpolations")

class ParticlesMenu(bpy.types.Menu):
    bl_idname = "an.particles_menu"
    bl_label = "Particles Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_ParticleSystemsInputNode", "Systems Input")
        insertNode(layout, "an_GetParticlesNode", "Get Particles")
        insertNode(layout, "an_FilterParticlesNode", "State Filter")
        insertNode(layout, "an_ParticlesInfoNode", "Particle List Info")
        insertNode(layout, "an_ParticleInfoNode", "Particle Info")

class SystemMenu(bpy.types.Menu):
    bl_idname = "an.system_menu"
    bl_label = "System Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_ConvertNode", "Convert")
        insertNode(layout, "an_DebugOutputNode", "Debug")



def insertNode(layout, type, text, settings = {}):
    operator = layout.operator("node.add_node", text = text)
    operator.type = type
    operator.use_transform = True
    for name, value in settings.items():
        item = operator.settings.add()
        item.name = name
        item.value = value
    return operator


class CreateNodeTree(bpy.types.Operator):
    bl_idname = "an.create_node_tree"
    bl_label = "Create Node Tree"
    bl_description = "Create a new Animation Node tree"
    bl_options = {"REGISTER"}

    def execute(self, context):
        nodeTree = bpy.data.node_groups.new(name = "NodeTree", type = "an_AnimationNodeTree")
        context.space_data.node_tree = nodeTree
        context.area.tag_redraw()
        return {"FINISHED"}


class SelectNodeTree(bpy.types.Operator):
    bl_idname = "an.select_node_tree"
    bl_label = "Select Node Tree"
    bl_description = "Select a Animation Node tree"
    bl_options = {"REGISTER"}

    nodeTreeName = bpy.props.StringProperty(default = "")

    def execute(self, context):
        nodeTree = bpy.data.node_groups.get(self.nodeTreeName)
        context.space_data.node_tree = nodeTree
        context.area.tag_redraw()
        return {"FINISHED"}


def registerMenu():
    bpy.types.NODE_MT_add.append(drawMenu)

def unregisterMenu():
    bpy.types.NODE_MT_add.remove(drawMenu)
