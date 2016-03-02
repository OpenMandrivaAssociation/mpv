# debuginfo-without-sources
%define debug_package %{nil}
%define major		1
%define libname		%mklibname %{name} %{major}
%define devname		%mklibname %{name} -d
# mrb build won't build in contrib without all repos, mrb included
#define distsuffix mrb

Summary:	Movie player playing most video formats and DVDs
Name:		mpv
Version:	0.16.0
Release:	1
License:	GPLv2+
Group:		Video
Url:		http://%{name}.io/
Source0:	https://github.com/%{name}-player/%{name}/archive/v%{version}.tar.gz
Source1:	http://ftp.waf.io/pub/release/waf-1.8.9
BuildRequires:	desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:	imagemagick
BuildRequires:	python-docutils
BuildRequires:	python-rst2pdf
BuildRequires:	texlive-caption
BuildRequires:	texlive-latex
BuildRequires:	texlive-cmap
BuildRequires:	texlive-preprint
BuildRequires:	ladspa-devel
BuildRequires:	ffmpeg-devel >= 2.5.4
BuildRequires:	jpeg-devel
BuildRequires:	krb5-devel
BuildRequires:	pkgconfig(libmng)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(libquvi)
BuildRequires:	pkgconfig(libv4lconvert)
BuildRequires:	linux-userspace-headers
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(caca)
BuildRequires:	pkgconfig(dri)
BuildRequires:	pkgconfig(dvdnav)
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(enca)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libbluray)
BuildRequires:	pkgconfig(libbs2b)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libcdio_cdda)
BuildRequires:	pkgconfig(libcdio_paranoia)
BuildRequires:	pkgconfig(libguess)
BuildRequires:	pkgconfig(libiso9660)
BuildRequires:	pkgconfig(libudf)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(libva-x11)
BuildRequires:	pkgconfig(luajit)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(smbclient)
BuildRequires:	pkgconfig(vdpau)
# wayland too old 
#BuildRequires:	pkgconfig(wayland-client)
#BuildRequires:	pkgconfig(wayland-cursor)
#BuildRequires:	pkgconfig(wayland-scanner)
#BuildRequires:	pkgconfig(wayland-server)
#BuildRequires:	pkgconfig(wayland-egl)
#BuildRequires:	wayland-tools

BuildRequires:	pkgconfig(libass) >= 0.12.1
BuildRequires:	pkgconfig(rubberband)  >= 1.8.0
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(zlib)
BuildRequires:  perl
BuildRequires:  yasm
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(ptlib)
BuildRequires:  pkgconfig(sdl2)

Requires:       hicolor-icon-theme

Suggests:	youtube-dl >= 2015.04.17

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
%dir %{_datadir}/zsh/site-functions
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
%{_includedir}/%{name}/qthelper.hpp
%{_includedir}/%{name}/opengl_cb.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------------

%prep
%setup -q
cp -R %{SOURCE1} waf && chmod +x waf

%build
LDFLAGS="%{ldflags} -lSDL" \
CCFLAGS="%{optflags}" \
./waf configure \
	--prefix="%{_prefix}" \
	--bindir="%{_bindir}" \
	--mandir="%{_mandir}" \
	--libdir="%{_libdir}" \
	--docdir="%{_docdir}/%{name}" \
	--confdir="%{_sysconfdir}/%{name}" \
	--disable-build-date \
	--disable-debug \
	--enable-openal \
	--enable-cdda \
	--enable-libmpv-shared \
	--disable-debug \
	--enable-sdl2 \
	--enable-pdf-build \
	--enable-zsh-comp 
	
./waf build --verbose

%install
./waf --destdir=%{buildroot} install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

