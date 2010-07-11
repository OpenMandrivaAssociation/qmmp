Name:		qmmp
Version:	0.4.1
Release:	%mkrel 1
License:	GPLv2+
URL:		http://qmmp.ylsoftware.com/index_en.php
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt4-devel >= 4.3
BuildRequires:	qt4-linguist
BuildRequires:	mad-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	libalsa-devel
BuildRequires:	taglib-devel
BuildRequires:	libcurl-devel
BuildRequires:	libflac-devel >= 1.1.3
BuildRequires:	libmpcdec-devel
BuildRequires:	jackit-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libwavpack-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	libprojectm-devel
BuildRequires:	libcdio-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	libcddb-devel
BuildRequires:	libmms-devel
BuildRequires:	libbs2b-devel
BuildRequires:	enca-devel
BuildRequires:	cmake

Source:		http://qmmp.ylsoftware.com/files/%{name}-%{version}.tar.bz2
Group:		Sound
Summary:	Qt-based Multimedia Player

%define major			0
%define libname 		%mklibname %{name}	%{major}
%define libname_devel		%mklibname %{name} 	-d
%define libnameui 		%mklibname qmmpui 	%{major}
%define libnameui_devel		%mklibname qmmpui 	-d
Requires:	unzip
Requires:	%{libname} = %{version}
Requires:	%{libnameui} = %{version}
Requires:	%name-plugins = %{version}


%description
This program is an audio-player, written with help of Qt library. The user
interface is similar to winamp or xmms.

Main opportunities:
* winamp and xmms skins support;
* plugins support;
* MPEG1 layer 1/2/3 support;
* Ogg Vorbis support;
* native FLAC support;
* Musepack support;
* WavePack support;
* ModPlug support;
* WMA support;
* PCM WAVE support;
* AlSA sound output;
* JACK sound output;
* OSS sound output;
* PulseAudio output;
* Last.fm scrobbler;
* D-Bus support;
* Spectrum Analyzer;
* sample rate conversion;
* streaming support (MP3, Vorbis via IceCast/ShoutCast).

%package -n	%{libname}
Group:		System/Libraries
Summary:	Library for %{name}
Conflicts:	%name < 0.2.0

%description -n	%{libname}
Qmmp is an audio-player, written with help of Qt library.
This package contains the library needed by %{name}

%package -n	%{libnameui}
Group:		System/Libraries
Summary:	Library for %{name}
Conflicts:      %name < 0.2.0

%description -n	%{libnameui}
Qmmp is an audio-player, written with help of Qt library.
This package contains the library needed by %{name}


%package -n	%{libname_devel}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{libname_devel}
Qmmp is an audio-player, written with help of Qt library.
This package contains the files needed for developing applications
which use %{name}


%package -n	%{libnameui_devel}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libnameui} = %{version}
Provides:	lib%{name}ui-devel = %{version}-%{release}
Provides:	%{name}ui-devel = %{version}-%{release}

%description -n	%{libnameui_devel}
Qmmp is an audio-player, written with help of Qt library.
This package contains the files needed for developing applications
which use %{name}

%package -n %name-jack
Summary: Qmmp Jack Output Plugin
Group: Sound
Conflicts:      %name < 0.2.0

%description -n %name-jack
This is the Jack Output Plugin for Qmmp

%package -n %name-oss
Summary: Qmmp OSS Output Plugin
Group: Sound
Conflicts:      %name < 0.2.0

%description -n %name-oss
This is the Jack OSS Plugin for Qmmp

%package -n %name-musepack
Summary: Qmmp MusePack Output Plugin
Group: Sound
Conflicts:      %name < 0.2.0

%description -n %name-musepack
This is the Musepack Input Plugin for Qmmp

%package -n %name-ffmpeg
Summary: Qmmp FFMPEG Input Plugin
Group: Sound
Conflicts:      %name < 0.2.0

%description -n %name-ffmpeg
This is the FFMPEG Input Plugin for Qmmp

%package -n %name-wavpack
Summary: Qmmp WavPack Input Plugin
Group: Sound
Conflicts:      %name < 0.2.0

%description -n %name-wavpack
This is the WavPack Input Plugin for Qmmp

%package -n %name-modplug
Summary: Qmmp Modplug Input Plugin
Group: Sound
Conflicts:      %name < 0.2.0

%description -n %name-modplug
This is the Modplug Input Plugin for Qmmp

%package -n %name-plugins
Summary: Qmmp Plugins
Group: Sound
Provides: %name-plugins
Conflicts:      %name < 0.2.0

%description -n %name-plugins
Qmmp is an audio-player, written with help of Qt library.
This contains basic plugin distribution.

%prep
%setup -q

%build
%cmake_qt4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

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
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/%name

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/libqmmp.so.%{major}*

%files -n %{libnameui}
%defattr(-,root,root,-)
%{_libdir}/libqmmpui.so.%{major}*

%files -n %{libname_devel}
%defattr(-,root,root,-)
%{_includedir}/%name/*
%{_libdir}/libqmmp.so

%files -n %{libnameui_devel}
%defattr(-,root,root,-)
%{_includedir}/qmmpui/*
%{_libdir}/libqmmpui.so

%files -n %name-jack
%{_libdir}/%name/Output/libjack.so

%files -n %name-oss
%{_libdir}/%name/Output/liboss.so

%files -n %name-musepack
%{_libdir}/%name/Input/libmpc.so

%files -n %name-ffmpeg
%{_libdir}/%name/Input/libffmpeg.so

%files -n %name-wavpack
%{_libdir}/%name/Input/libwavpack.so

%files -n %name-modplug
%{_libdir}/%name/Input/libmodplug.so

%files -n %name-plugins
%{_libdir}/%name/Input/libflac.so
%{_libdir}/%name/Input/libmad.so
%{_libdir}/%name/Input/libsndfile.so
%{_libdir}/%name/Input/libvorbis.so
%{_libdir}/%name/Input/libcdaudio.so
%{_libdir}/%name/Input/libcue.so

%{_libdir}/%name/Output/libalsa.so
%{_libdir}/%name/Output/libpulseaudio.so
%{_libdir}/%name/Output/libnull.so

%{_libdir}/%name/General/libnotifier.so
%{_libdir}/%name/General/libscrobbler.so
%{_libdir}/%name/General/libstatusicon.so
%{_libdir}/%name/General/libfileops.so
%{_libdir}/%name/General/libhal.so
%{_libdir}/%name/General/libhotkey.so
%{_libdir}/%name/General/liblyrics.so
%{_libdir}/%name/General/libmpris.so
%{_libdir}/%name/General/libcovermanager.so
%{_libdir}/%name/General/libkdenotify.so

%{_libdir}/%name/Engines/libmplayer.so

%{_libdir}/%name/CommandLineOptions/libincdecvolumeoption.so
%{_libdir}/%name/CommandLineOptions/libseekoption.so
%{_libdir}/%name/Effect/libsrconverter.so
%{_libdir}/%name/Effect/libbs2b.so
%{_libdir}/%name/Effect/libladspa.so
%{_libdir}/%name/FileDialogs/libqmmpfiledialog.so
%{_libdir}/%name/PlaylistFormats/libm3uplaylistformat.so
%{_libdir}/%name/PlaylistFormats/libplsplaylistformat.so
%{_libdir}/%name/PlaylistFormats/libxspfplaylistformat.so
%{_libdir}/%name/Transports/libhttp.so
%{_libdir}/%name/Transports/libmms.so
%{_libdir}/%name/Visual/libanalyzer.so
%{_libdir}/%name/Visual/libprojectm.so
