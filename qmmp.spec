Name:		qmmp
Version:	0.1.6
Release:	%mkrel 1
License:	GPLv2+
URL:		http://qmmp.ylsoftware.com
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt4-devel
BuildRequires:	mad-devel
BuildRequires:	oggvorbis-devel liboggflac-devel
BuildRequires:	libalsa-devel
BuildRequires:	taglib-devel
BuildRequires:	jackit-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libmpcdec-devel
Source:		http://qmmp.ylsoftware.com/files/%{name}-%{version}.tar.bz2
Patch0:		qmmp-0.1.6-new-ffmpeg-header-location.patch
Group:		Sound
Summary:	Qt-based Multimedia Player

%description
This program is an audio-player, written with help of Qt library. The user
interface is similar to winamp or xmms.

Main opportunities:
* winamp and xmms skins support;
* plugins support;
* MPEG1 layer 1/2/3 support;
* Ogg Vorbis support;
* Native FLAC support;
* Musepack support;
* WMA support;
* AlSA sound output;
* JACK sound output.

%prep
%setup -q
%patch0 -p0

%build
%qmake_qt4
make

%install
rm -fr %buildroot
make install INSTALL_ROOT=%{buildroot}%{_prefix}

# move /usr/lib to /usr/lib64
%if "%{_libdir}" == "/usr/lib64"
	mv %buildroot%_prefix/lib %buildroot%_libdir
%endif

rm -f %buildroot%_libdir/*.so

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%{_bindir}/%{name}
%{_libdir}/*.so.*
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
