from prova import write_igb, read_igb
import numpy as np


def fibers_vec(alpha,phi,gamma):
    f_x= np.cos(alpha)*np.sin(phi)+np.sin(alpha)*np.cos(gamma)*np.cos(phi)
    f_y=-np.cos(alpha)*np.cos(phi)+np.sin(alpha)*np.cos(gamma)*np.sin(phi)
    f_z=-np.sin(alpha)*np.sin(gamma)
    return np.array((f_x,f_y,f_z)).T

fib=fibers_vec(np.pi/2,np.pi/2,0)
fib3=fibers_vec(0,np.pi,0)

Nx,Ny,Nz= 10,10,10
z=np.linspace(0,10,10)
cellu=np.full((Nx,Ny,Nz),z)
alpha=np.full((Nx,Ny,Nz),np.pi/20*z)
gamma=np.full((Nx,Ny,Nz),0.0-np.pi/20*z)
phi=np.full((Nx,Ny,Nz),np.pi/2-np.pi/20*z)
#rotation from x to z

alpha1=np.full((Nx,Ny,Nz),np.pi/2)
phi1=np.full((Nx,Ny,Nz),np.pi/2-(np.pi/20)*z)
gamma1=np.full((Nx,Ny,Nz),0.0-np.pi/20*z)

alpha2=np.full((Nx,Ny,Nz),-np.pi/20*z)
gamma2=np.full((Nx,Ny,Nz),0.0+np.pi/20*z)
phi2=np.full((Nx,Ny,Nz),-np.pi/2+np.pi/20*z)

write_igb(cellu,'cellu.igb')

write_igb(alpha,'alpha.igb',convert_angles=True)
write_igb(gamma,'gamma.igb',convert_angles=True)
write_igb(phi,'phi.igb',convert_angles=True)


#(cos(vmfa)*sin(vmfp)+sin(vmfa)*cos(vmfg)*cos(vmfp))*iHat+(-cos(vmfa)*cos(vmfp)+sin(vmfa)*cos(vmfg)*sin(vmfp))*jHat+(-sin(vmfa)*sin(vmfg))*kHat

write_igb(alpha1,'alpha1.igb',convert_angles=True)
write_igb(gamma1,'gamma1.igb',convert_angles=True)
write_igb(phi1,'phi1.igb',convert_angles=True)

write_igb(alpha2,'alpha2.igb',convert_angles=True)
write_igb(gamma2,'gamma2.igb',convert_angles=True)
write_igb(phi2,'phi2.igb',convert_angles=True)



#different scaling
nx,ny,nz= 20,20,20
z=np.linspace(0,20,20)
cell1=np.full((nx,ny,nz),z)
alpha3=np.full((nx,ny,nz),np.pi/40*z)
gamma3=np.full((nx,ny,nz),0.0-np.pi/40*z)
phi3=np.full((nx,ny,nz),np.pi/2-np.pi/40*z)
write_igb(cell1,'cell1.igb')
write_igb(alpha3,'alpha3.igb',convert_angles=True)
write_igb(gamma3,'gamma3.igb',convert_angles=True)
write_igb(phi3,'phi3.igb',convert_angles=True)



#rotation on the same plane
z=np.linspace(0,10,10)
cell2=np.full((Nx,Ny,Nz),z)
x=np.linspace(0,10,10)
y=np.linspace(0,10,10)
alpha5=np.full((Nx,Ny,Nz),0.0+(np.sqrt(np.cos(np.pi/20*x)**2+np.sin(np.pi/20*y)**2))*np.pi/20*z)
gamma4=np.full((Nx,Ny,Nz),0.0)
phi4=np.full((Nx,Ny,Nz),np.pi/2)
write_igb(cell2,'cells.igb')
write_igb(alpha5,'alphaaa.igb',convert_angles=True)
write_igb(gamma4,'gammma4.igb',convert_angles=True)
write_igb(phi4,'phii4.igb',convert_angles=True)