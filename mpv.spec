%define debug_package %{nil}
%define major		1
%define libname		%mklibname %{name} %{major}
%define devname		%mklibname %{name} -d

Name:           mpv
Version:        0.11.0
Release:        1
Summary:        Movie player playing most video formats and DVDs
Group:		Video
License:        GPLv2+
URL:            http://%{name}.io/
Source0:        https://github.com/%{name}-player/%{name}/archive/v%{version}.tar.gz
# latest stable waf
Source1:        https://waf.io/pub/release/waf-1.8.12


BuildRequires:  hicolor-icon-theme
BuildRequires:  ladspa-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  jpeg-devel
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libquvi)
BuildRequires:  pkgconfig(libv4lconvert)
BuildRequires:  pkgconfig(liblircclient0)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(caca)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(enca)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_cdda)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libiso9660)
BuildRequires:  pkgconfig(libudf)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  texlive-cmap
BuildRequires:  texlive-preprint
BuildRequires:  texlive-caption
BuildRequires:  texlive-latex
BuildRequires:  pkgconfig(libguess)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  krb5-devel
BuildRequires:  desktop-file-utils
BuildRequires:  imagemagick 
BuildRequires:	python2-docutils
BuildRequires:	python-docutils
BuildRequires:	linux-userspace-headers

Requires:       hicolor-icon-theme

Suggests:	youtube-dl >= 2015.01.16


%description
Mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types. Special
input URL types are available to read input from a variety of sources other
than disk files. Depending on platform, a variety of different video and audio
output methods are supported.


%files
%doc LICENSE README.md Copyright etc/example.conf etc/input.conf
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/zsh/site-functions/_mpv
%{_mandir}/man1/%{name}.*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/encoding-profiles.conf

#------------------------------------
%package -n %{libname}
Summary:	Library for %{name}
Group:		System/Libraries

%description -n %{libname}
Mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types. Special
input URL types are available to read input from a variety of sources other
than disk files. Depending on platform, a variety of different video and audio
output methods are supported.

%files -n %{libname}
%doc LICENSE README.md Copyright
%{_libdir}/*.so.*

#------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types. Special
input URL types are available to read input from a variety of sources other
than disk files. Depending on platform, a variety of different video and audio
output methods are supported.

%files -n %{devname}
%doc LICENSE README.md Copyright
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/client.h
%{_includedir}/%{name}/opengl_cb.h
%{_includedir}/%{name}/qthelper.hpp
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

cp %{SOURCE1} waf
chmod 0755 waf

%build
CCFLAGS="%{optflags}" \
./waf configure \
	--prefix="%{_prefix}" \
	--bindir="%{_bindir}" \
	--mandir="%{_mandir}" \
	--libdir="%{_libdir}" \
	--docdir="%{_docdir}/%{name}" \
	--confdir="%{_sysconfdir}/%{name}" \
	--disable-sdl1 --disable-sdl2 \
	--disable-build-date \
	--disable-debug \
	--enable-openal \
	--enable-cdda \
	--enable-libmpv-shared \
	--enable-zsh-comp
    
./waf build --verbose 

%install
./waf --destdir=%{buildroot} install 

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop



