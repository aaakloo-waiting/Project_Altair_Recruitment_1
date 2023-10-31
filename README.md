# Project_Altair_Recruitment_1
 First & Second week's(online) challenges of the recruitment process of IUT_Mars_Rover: software_sub_team-2023


<?xml version ="1.0"?>

<robot name="Four_Wheeler_dd_robot" xmlns:xacro="http://www.ros.org/wiki/xacro">

<!--Body Dimension-->
<xacro:property name="body_link_x_dim" value="1"/>
<xacro:property name="body_link_y_dim" value="0.6"/>
<xacro:property name="body_link_z_dim" value="0.3"/>

<!--Wheel Dimension-->
<xacro:property name="wheel_link_radius" value="0.15"/>
<xacro:property name="wheel_link_length" value="0.1"/>
<xacro:property name="body_link_z_loaction" value="-0.1"/>

<!--Material Density-->
<xacro:property name="body_density" value="2710.0"/>
<xacro:property name="wheel_density" value="2710.0"/>

<xacro:property name="pi_const" value="3.14159265"/>

<!--Body Mass-->
<xacro:property name="body_mass" value="${body_density*body_link_x_dim*body_link_y_dim*body_link_z_dim}"/>
<!--Wheel Mass-->
<xacro:property name="wheel_mass" value="${wheel_density*pi_const*wheel_link_radius*wheel_link_radius*wheel_link_length}"/>

<!--Moments of Inertia of wheel (I)-->
<xacro:property name="Iz_wheel" value="${0.5*wheel_mass*wheel_link_radius*wheel_link_radius}"/>
<xacro:property name="I_wheel" value="${(1.0/12.0)*wheel_mass*(3.0*wheel_link_radius*wheel_link_radius+wheel_link_length*wheel_link_length)}"/>


<xacro:macro name="inertia_wheel">
	<inertial>
		<origin rpy="0 0 0" xyz="0 0 0"/>
		<mass value="${wheel_mass}"/>
		<inertia ixx="${I_wheel}" ixy="0.0" ixz="0.0" iyy="${I_wheel}" iyz="0" izz="Iz_wheel"/>
	</inertial>
</xacro:macro>

<xacro:include filename="$(find robot_model_pkg)/urdf/robot.gazebo"/>

<link name="dummy">
</link>

<joint name="dummy_joint" type="fixed">
	<parent link="dummy"/>
	<child link="body_link"/>
</joint>

<link name="body_link">
	<visual>
		<geometry>
			<box size="${body_link_x_dim} ${body_link_y_dim} ${body_link_z_dim}" />
		</geometry>
		<origin rpy="0 0 0" xyz="0 0 0" />
	</visual>
			
	<collision>
		<geometry>
			<box size="${body_link_x_dim} ${body_link_y_dim} ${body_link_z_dim}" />
		</geometry>
		<origin rpy="0 0 0" xyz="0 0 0" />	
	</collision>	
	
	<inertial>
		<origin rpy="0 0 0" xyz="0 0 0" />
		<mass value="${body_mass}"/>
		<inertia 
		ixx="${(1/12)*body_mass*(body_link_y_dim*body_link_y_dim + body_link_z_dim*body_link_z_dim)}" ixy="0" 			ixz="0" iyy="${(1/12)*body_mass*(body_link_x_dim*body_link_x_dim + body_link_z_dim*body_link_z_dim)}" 
		iyz="0" izz="${(1/12)*body_mass*(body_link_y_dim*body_link_y_dim + body_link_x_dim*body_link_x_dim)}"/>
	</inertial>
</link>	
