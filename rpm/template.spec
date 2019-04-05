Name:           ros-indigo-xpp
Version:        1.0.10
Release:        0%{?dist}
Summary:        ROS xpp package

Group:          Development/Libraries
License:        BSD
URL:            http://github.com/leggedrobotics/xpp
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-xpp-examples
Requires:       ros-indigo-xpp-hyq
Requires:       ros-indigo-xpp-msgs
Requires:       ros-indigo-xpp-quadrotor
Requires:       ros-indigo-xpp-states
Requires:       ros-indigo-xpp-vis
BuildRequires:  ros-indigo-catkin

%description
Visualization of motion-plans for legged robots. It draws support areas, contact
forces and motion trajectories in RVIZ and displays URDFs for specific robots,
including a one-legged, a two-legged hopper and HyQ. Example motions were
generated by towr.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Apr 05 2019 Alexander W. Winkler <alexander.w.winkler@gmail.com> - 1.0.10-0
- Autogenerated by Bloom

* Tue Jul 10 2018 Alexander W. Winkler <winklera@ethz.ch> - 1.0.9-0
- Autogenerated by Bloom

* Wed Apr 18 2018 Alexander W. Winkler <winklera@ethz.ch> - 1.0.6-0
- Autogenerated by Bloom

* Thu Feb 01 2018 Alexander W. Winkler <winklera@ethz.ch> - 1.0.5-0
- Autogenerated by Bloom

* Wed Jan 03 2018 Alexander W. Winkler <winklera@ethz.ch> - 1.0.4-0
- Autogenerated by Bloom

* Fri Nov 03 2017 Alexander W. Winkler <winklera@ethz.ch> - 1.0.3-0
- Autogenerated by Bloom

* Fri Oct 27 2017 Alexander W. Winkler <winklera@ethz.ch> - 1.0.1-1
- Autogenerated by Bloom

* Fri Oct 27 2017 Alexander W. Winkler <winklera@ethz.ch> - 1.0.1-0
- Autogenerated by Bloom

* Thu Oct 26 2017 Alexander W. Winkler <winklera@ethz.ch> - 1.0.0-1
- Autogenerated by Bloom

* Thu Oct 26 2017 Alexander W. Winkler <winklera@ethz.ch> - 1.0.0-0
- Autogenerated by Bloom

