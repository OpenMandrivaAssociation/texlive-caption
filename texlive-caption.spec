Name:		texlive-caption
Epoch:		1
Version:	68425
Release:	1
Summary:	Customising captions in floating environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/caption
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/caption.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/caption.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/caption.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The caption package provides many ways to customise the
captions in floating environments like figure and table, and
cooperates with many other packages. Facilities include
rotating captions, sideways captions, continued captions (for
tables or figures that come in several parts). A list of
compatibility notes, for other packages, is provided in the
documentation. The package also provides the "caption outside
float" facility, in the same way that simpler packages like
capt-of do. The package supersedes caption2.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/caption
%doc %{_texmfdistdir}/doc/latex/caption
#- source
%doc %{_texmfdistdir}/source/latex/caption

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
