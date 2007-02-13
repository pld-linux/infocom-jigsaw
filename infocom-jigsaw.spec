%define		_name		Jigsaw
Summary:	Infocom text game - Jigsaw
Summary(pl.UTF-8):	Tekstówka Infocomu - Jigsaw
Name:		infocom-jigsaw
Version:	951129
Release:	2
License:	free
Group:		Applications/Games
Source0:	ftp://ftp.ifarchive.org/if-archive/games/zcode/%{_name}.z8
# Source0-md5:	1bf8b3f6edbffb0f83bb61dbb56dd17d
URL:		http://www.ifarchive.org/
Requires:	zcode-wrapper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
New Year's Eve, 1999, a quarter to midnight and where else to be but
Century Park! Fireworks cascadeacross the sky, your stomach rumbles
uneasily, music and lasers howl across the parkland... Not exactly
your ideal party (especially as that rather attractive stranger in
black has slipped back into the crowds) - but cheer up, you won't live
to see the next.

%description -l pl.UTF-8
Sylwester 1999, kwadrans przed północą - gdzież można być, jak nie w
Parku Stulecia (Century Park)! Zimne ognie rozpryskują się na niebie,
nieprzyjemnie burczy ci w brzuchu, muzyka i lasery wyją w całym
parku... Twoja niekoniecznie idealna partnerka (zwłaszcza, że ta
całkiem atrakcyjna nieznajoma w czerni ponownie zlała się z tłumem) -
ale rozchmurz się, nie będziesz czekać aż ujrzysz następną.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/zcode}

cp %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/games/zcode
ln -s %{_datadir}/games/zcode/wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/zcode/*.z8
