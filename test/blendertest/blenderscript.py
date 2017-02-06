import bpy
import bmesh

for ob in bpy.data.objects:
    if ob.name.startswith('structure'):
        ob.select = True
bpy.ops.object.delete()
for me in bpy.data.meshes:
    if me.name.startswith('structure'):
        bpy.data.meshes.remove(me)
for mat in bpy.data.materials:
    if mat.name.startswith('structure'):
        bpy.data.materials.remove(mat)
nonshinyblack = bpy.data.materials.new('structure.material.nonshinyblack')
nonshinyblack.diffuse_color = (0, 0, 0)
nonshinyblack.specular_color = (0, 0, 0)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 6, diameter1 =     0.0500, diameter2 =     0.0500, depth =     9.9416)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     4.9708))
mesh = bpy.data.meshes.new('structure.meshXAxis_cylinder')
bm.to_mesh(mesh)
mesh.materials.append(nonshinyblack)
ob = bpy.data.objects.new('structure.XAxis_cylinder', mesh)
ob.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob.data.transform([[    1.0000,     0.0000,     0.0000,     0.0000], \
 [   -0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
bpy.context.scene.objects.link(ob)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 24, diameter1 =     0.2000, diameter2 =     0.0100, depth =     0.5000)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,    10.1916))
mesh = bpy.data.meshes.new('structure.meshXAxis_cone')
bm.to_mesh(mesh)
mesh.materials.append(nonshinyblack)
ob = bpy.data.objects.new('structure.XAxis_cone', mesh)
ob.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob.data.transform([[    1.0000,     0.0000,     0.0000,     0.0000], \
 [   -0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
bpy.context.scene.objects.link(ob)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 6, diameter1 =     0.0500, diameter2 =     0.0500, depth =     9.9416)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     4.9708))
mesh = bpy.data.meshes.new('structure.meshYAxis_cylinder')
bm.to_mesh(mesh)
mesh.materials.append(nonshinyblack)
ob = bpy.data.objects.new('structure.YAxis_cylinder', mesh)
ob.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob.data.transform([[   -0.5000,     0.8660,     0.0000,     0.0000], \
 [   -0.8660,    -0.5000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
bpy.context.scene.objects.link(ob)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 24, diameter1 =     0.2000, diameter2 =     0.0100, depth =     0.5000)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,    10.1916))
mesh = bpy.data.meshes.new('structure.meshYAxis_cone')
bm.to_mesh(mesh)
mesh.materials.append(nonshinyblack)
ob = bpy.data.objects.new('structure.YAxis_cone', mesh)
ob.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob.data.transform([[   -0.5000,     0.8660,     0.0000,     0.0000], \
 [   -0.8660,    -0.5000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
bpy.context.scene.objects.link(ob)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 6, diameter1 =     0.0500, diameter2 =     0.0500, depth =     5.8432)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     2.9216))
mesh = bpy.data.meshes.new('structure.meshZAxis_cylinder')
bm.to_mesh(mesh)
mesh.materials.append(nonshinyblack)
ob = bpy.data.objects.new('structure.ZAxis_cylinder', mesh)
ob.data.transform([[    1.0000,     0.0000,    -0.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob.data.transform([[    0.5000,     0.8660,     0.0000,     0.0000], \
 [   -0.8660,     0.5000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
bpy.context.scene.objects.link(ob)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 24, diameter1 =     0.2000, diameter2 =     0.0100, depth =     0.5000)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     6.0932))
mesh = bpy.data.meshes.new('structure.meshZAxis_cone')
bm.to_mesh(mesh)
mesh.materials.append(nonshinyblack)
ob = bpy.data.objects.new('structure.ZAxis_cone', mesh)
ob.data.transform([[    1.0000,     0.0000,    -0.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob.data.transform([[    0.5000,     0.8660,     0.0000,     0.0000], \
 [   -0.8660,     0.5000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
bpy.context.scene.objects.link(ob)
bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.delete(type='VERT')
bpy.ops.object.mode_set(mode='OBJECT')
posobject = bpy.context.object
posobject.name = 'structure.Positions'
bpy.ops.mesh.primitive_ico_sphere_add(location=(0,0,0), size=0.292400)
ob = bpy.context.object
me = ob.data
me.name = 'structure.mesh.Mn'
bpy.ops.object.delete()
mat = bpy.data.materials.new('structure.material.Mn')
mat.diffuse_color = (0.6118, 0.4784, 0.7804)
me.materials.append(mat)
bpy.ops.mesh.primitive_ico_sphere_add(location=(0,0,0), size=0.200000)
ob = bpy.context.object
me = ob.data
me.name = 'structure.mesh.O'
bpy.ops.object.delete()
mat = bpy.data.materials.new('structure.material.O')
mat.diffuse_color = (1.0, 0.051, 0.051)
me.materials.append(mat)
bpy.ops.mesh.primitive_ico_sphere_add(location=(0,0,0), size=0.271400)
ob = bpy.context.object
me = ob.data
me.name = 'structure.mesh.Ca'
bpy.ops.object.delete()
mat = bpy.data.materials.new('structure.material.Ca')
mat.diffuse_color = (0.2392, 1.0, 0.0)
me.materials.append(mat)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.220800, 6.028461, 1.057200)
ob = bpy.data.objects.new(             'structure.Atom001(Mn2)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (5.220800, 6.028461, 1.057200)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (6.119300, 5.483789, 2.630736)
ob = bpy.data.objects.new(             'structure.Atom002(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (6.119300, 5.483789, 2.630736)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.220800, 3.014230, 5.286000)
ob = bpy.data.objects.new(             'structure.Atom003(Mn3)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (5.220800, 3.014230, 5.286000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.610400, 4.521345, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom004(Mn1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.610400, 4.521345, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 3.014230, 2.114400)
ob = bpy.data.objects.new(             'structure.Atom005(Mn1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (0.000000, 3.014230, 2.114400)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.220800, 3.014230, 2.114400)
ob = bpy.data.objects.new(             'structure.Atom006(Ca1)', bpy.data.meshes['structure.mesh.Ca'])
ob.location = (5.220800, 3.014230, 2.114400)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 0.000000, 6.343200)
ob = bpy.data.objects.new(             'structure.Atom007(Ca1)', bpy.data.meshes['structure.mesh.Ca'])
ob.location = (0.000000, 0.000000, 6.343200)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.610400, 1.507115, 4.228800)
ob = bpy.data.objects.new(             'structure.Atom008(Mn1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.610400, 1.507115, 4.228800)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.220800, 0.000000, 6.343200)
ob = bpy.data.objects.new(             'structure.Atom009(Mn1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (5.220800, 0.000000, 6.343200)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.220800, 6.028461, 4.228800)
ob = bpy.data.objects.new(             'structure.Atom010(Mn1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (5.220800, 6.028461, 4.228800)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.929315, 4.401590, 6.391831)
ob = bpy.data.objects.new(             'structure.Atom011(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (5.929315, 4.401590, 6.391831)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-5.220800, 9.042691, 3.171600)
ob = bpy.data.objects.new(             'structure.Atom012(Mn3)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-5.220800, 9.042691, 3.171600)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.610400, 4.521345, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom013(Mn1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-2.610400, 4.521345, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (9.594369, 1.307272, 2.065769)
ob = bpy.data.objects.new(             'structure.Atom014(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (9.594369, 1.307272, 2.065769)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.220800, 0.000000, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom015(Mn1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (5.220800, 0.000000, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.898500, 2.469559, 0.516336)
ob = bpy.data.objects.new(             'structure.Atom016(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (0.898500, 2.469559, 0.516336)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-3.665054, 9.122779, 2.065769)
ob = bpy.data.objects.new(             'structure.Atom017(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-3.665054, 9.122779, 2.065769)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-1.555746, 5.948372, 2.163031)
ob = bpy.data.objects.new(             'structure.Atom018(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-1.555746, 5.948372, 2.163031)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 0.000000, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom019(Ca1)', bpy.data.meshes['structure.mesh.Ca'])
ob.location = (0.000000, 0.000000, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 3.014230, 5.286000)
ob = bpy.data.objects.new(             'structure.Atom020(Mn2)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (0.000000, 3.014230, 5.286000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.610400, 7.535576, 2.114400)
ob = bpy.data.objects.new(             'structure.Atom021(Mn1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-2.610400, 7.535576, 2.114400)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (10.441600, 0.000000, 6.343200)
ob = bpy.data.objects.new(             'structure.Atom022(Ca1)', bpy.data.meshes['structure.mesh.Ca'])
ob.location = (10.441600, 0.000000, 6.343200)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.831200, 4.521345, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom023(Mn1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (7.831200, 4.521345, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (6.068031, 1.706959, 6.391831)
ob = bpy.data.objects.new(             'structure.Atom024(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (6.068031, 1.706959, 6.391831)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-0.898500, 3.558902, 3.712464)
ob = bpy.data.objects.new(             'structure.Atom025(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-0.898500, 3.558902, 3.712464)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-4.373569, 7.735419, 4.277431)
ob = bpy.data.objects.new(             'structure.Atom026(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-4.373569, 7.735419, 4.277431)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.610400, 7.535576, 5.286000)
ob = bpy.data.objects.new(             'structure.Atom027(Mn2)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.610400, 7.535576, 5.286000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-1.689451, 8.041364, 3.712464)
ob = bpy.data.objects.new(             'structure.Atom028(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-1.689451, 8.041364, 3.712464)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-0.847231, 7.335732, 6.294569)
ob = bpy.data.objects.new(             'structure.Atom029(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-0.847231, 7.335732, 6.294569)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (6.068031, 1.706959, 0.048631)
ob = bpy.data.objects.new(             'structure.Atom030(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (6.068031, 1.706959, 0.048631)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (1.555746, 6.108549, 6.294569)
ob = bpy.data.objects.new(             'structure.Atom031(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (1.555746, 6.108549, 6.294569)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.587951, 0.456656, 5.826864)
ob = bpy.data.objects.new(             'structure.Atom032(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (2.587951, 0.456656, 5.826864)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (3.665054, 8.962603, 4.277431)
ob = bpy.data.objects.new(             'structure.Atom033(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (3.665054, 8.962603, 4.277431)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-3.531349, 7.029788, 0.516336)
ob = bpy.data.objects.new(             'structure.Atom034(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-3.531349, 7.029788, 0.516336)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-5.220800, 9.042691, 6.343200)
ob = bpy.data.objects.new(             'structure.Atom035(Ca1)', bpy.data.meshes['structure.mesh.Ca'])
ob.location = (-5.220800, 9.042691, 6.343200)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (6.910251, 1.001327, 2.630736)
ob = bpy.data.objects.new(             'structure.Atom036(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (6.910251, 1.001327, 2.630736)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.220800, 9.042691, 6.343200)
ob = bpy.data.objects.new(             'structure.Atom037(Ca1)', bpy.data.meshes['structure.mesh.Ca'])
ob.location = (5.220800, 9.042691, 6.343200)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (3.665054, 2.934142, 6.391831)
ob = bpy.data.objects.new(             'structure.Atom038(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (3.665054, 2.934142, 6.391831)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.610400, 4.521345, 6.343200)
ob = bpy.data.objects.new(             'structure.Atom039(Mn1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-2.610400, 4.521345, 6.343200)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.831200, 1.507115, 1.057200)
ob = bpy.data.objects.new(             'structure.Atom040(Mn2)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (7.831200, 1.507115, 1.057200)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (4.322300, 0.544671, 1.598064)
ob = bpy.data.objects.new(             'structure.Atom041(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (4.322300, 0.544671, 1.598064)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (8.752149, 2.012903, 5.826864)
ob = bpy.data.objects.new(             'structure.Atom042(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (8.752149, 2.012903, 5.826864)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (3.531349, 5.027133, 1.598064)
ob = bpy.data.objects.new(             'structure.Atom043(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (3.531349, 5.027133, 1.598064)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (6.776546, 3.094318, 4.180169)
ob = bpy.data.objects.new(             'structure.Atom044(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (6.776546, 3.094318, 4.180169)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-0.708515, 4.641101, 6.294569)
ob = bpy.data.objects.new(             'structure.Atom045(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-0.708515, 4.641101, 6.294569)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (6.068031, 7.735419, 4.277431)
ob = bpy.data.objects.new(             'structure.Atom046(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (6.068031, 7.735419, 4.277431)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.808751, 3.470886, 1.598064)
ob = bpy.data.objects.new(             'structure.Atom047(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (7.808751, 3.470886, 1.598064)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (4.512285, 7.655331, 2.065769)
ob = bpy.data.objects.new(             'structure.Atom048(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (4.512285, 7.655331, 2.065769)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-5.220800, 9.042691, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom049(Ca1)', bpy.data.meshes['structure.mesh.Ca'])
ob.location = (-5.220800, 9.042691, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.831200, 4.521345, 6.343200)
ob = bpy.data.objects.new(             'structure.Atom050(Mn1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (7.831200, 4.521345, 6.343200)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (1.555746, 0.080088, 2.065769)
ob = bpy.data.objects.new(             'structure.Atom051(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (1.555746, 0.080088, 2.065769)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.898500, 8.498019, 4.745136)
ob = bpy.data.objects.new(             'structure.Atom052(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (0.898500, 8.498019, 4.745136)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (10.441600, 0.000000, 3.171600)
ob = bpy.data.objects.new(             'structure.Atom053(Mn3)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (10.441600, 0.000000, 3.171600)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.587951, 5.571805, 4.745136)
ob = bpy.data.objects.new(             'structure.Atom054(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-2.587951, 5.571805, 4.745136)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (1.689451, 4.015558, 4.745136)
ob = bpy.data.objects.new(             'structure.Atom055(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (1.689451, 4.015558, 4.745136)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (4.373569, 4.321502, 4.180169)
ob = bpy.data.objects.new(             'structure.Atom056(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (4.373569, 4.321502, 4.180169)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 6.028461, 4.228800)
ob = bpy.data.objects.new(             'structure.Atom057(Ca1)', bpy.data.meshes['structure.mesh.Ca'])
ob.location = (0.000000, 6.028461, 4.228800)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.610400, 1.507115, 1.057200)
ob = bpy.data.objects.new(             'structure.Atom058(Mn2)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.610400, 1.507115, 1.057200)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 9.042691, 3.171600)
ob = bpy.data.objects.new(             'structure.Atom059(Mn2)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (0.000000, 9.042691, 3.171600)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (4.322300, 6.573132, 5.826864)
ob = bpy.data.objects.new(             'structure.Atom060(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (4.322300, 6.573132, 5.826864)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (10.441600, 0.000000, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom061(Ca1)', bpy.data.meshes['structure.mesh.Ca'])
ob.location = (10.441600, 0.000000, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.831200, 4.521345, 3.171600)
ob = bpy.data.objects.new(             'structure.Atom062(Mn2)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (7.831200, 4.521345, 3.171600)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.632849, 8.586035, 0.516336)
ob = bpy.data.objects.new(             'structure.Atom063(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (2.632849, 8.586035, 0.516336)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 9.042691, 6.343200)
ob = bpy.data.objects.new(             'structure.Atom064(Mn1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (0.000000, 9.042691, 6.343200)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.847231, 4.721189, 2.163031)
ob = bpy.data.objects.new(             'structure.Atom065(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (0.847231, 4.721189, 2.163031)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.929315, 4.401590, 0.048631)
ob = bpy.data.objects.new(             'structure.Atom066(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (5.929315, 4.401590, 0.048631)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.831200, 1.507115, 4.228800)
ob = bpy.data.objects.new(             'structure.Atom067(Mn1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (7.831200, 1.507115, 4.228800)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.610400, 7.535576, 5.286000)
ob = bpy.data.objects.new(             'structure.Atom068(Mn2)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-2.610400, 7.535576, 5.286000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.708515, 1.387360, 4.277431)
ob = bpy.data.objects.new(             'structure.Atom069(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (0.708515, 1.387360, 4.277431)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.610400, 4.521345, 3.171600)
ob = bpy.data.objects.new(             'structure.Atom070(Mn2)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.610400, 4.521345, 3.171600)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.587951, 6.485116, 3.712464)
ob = bpy.data.objects.new(             'structure.Atom071(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (2.587951, 6.485116, 3.712464)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.610400, 4.521345, 3.171600)
ob = bpy.data.objects.new(             'structure.Atom072(Mn2)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-2.610400, 4.521345, 3.171600)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.632849, 2.557574, 2.630736)
ob = bpy.data.objects.new(             'structure.Atom073(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (2.632849, 2.557574, 2.630736)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.610400, 7.535576, 2.114400)
ob = bpy.data.objects.new(             'structure.Atom074(Mn1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.610400, 7.535576, 2.114400)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.220800, 0.000000, 3.171600)
ob = bpy.data.objects.new(             'structure.Atom075(Mn2)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (5.220800, 0.000000, 3.171600)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.220800, 9.042691, 3.171600)
ob = bpy.data.objects.new(             'structure.Atom076(Mn3)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (5.220800, 9.042691, 3.171600)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (3.665054, 2.934142, 0.048631)
ob = bpy.data.objects.new(             'structure.Atom077(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (3.665054, 2.934142, 0.048631)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.610400, 4.521345, 6.343200)
ob = bpy.data.objects.new(             'structure.Atom078(Mn1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.610400, 4.521345, 6.343200)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (4.512285, 1.626871, 4.180169)
ob = bpy.data.objects.new(             'structure.Atom079(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (4.512285, 1.626871, 4.180169)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 0.000000, 3.171600)
ob = bpy.data.objects.new(             'structure.Atom080(Mn3)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (0.000000, 0.000000, 3.171600)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 6.028461, 1.057200)
ob = bpy.data.objects.new(             'structure.Atom081(Mn3)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (0.000000, 6.028461, 1.057200)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.708515, 7.415820, 2.163031)
ob = bpy.data.objects.new(             'structure.Atom082(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (0.708515, 7.415820, 2.163031)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 9.042691, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom083(Mn1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (0.000000, 9.042691, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.220800, 9.042691, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom084(Ca1)', bpy.data.meshes['structure.mesh.Ca'])
ob.location = (5.220800, 9.042691, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
