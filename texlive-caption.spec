Name:		texlive-caption
Version:	3.2c
Release:	1
Summary:	Customising captions in floating environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/caption
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/caption.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/caption.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/caption.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/caption/bicaption.sty
%{_texmfdistdir}/tex/latex/caption/caption.sty
%{_texmfdistdir}/tex/latex/caption/caption2.sty
%{_texmfdistdir}/tex/latex/caption/caption3.sty
%{_texmfdistdir}/tex/latex/caption/ltcaption.sty
%{_texmfdistdir}/tex/latex/caption/subcaption.sty
%doc %{_texmfdistdir}/doc/latex/caption/README
%doc %{_texmfdistdir}/doc/latex/caption/bicaption.pdf
%doc %{_texmfdistdir}/doc/latex/caption/caption-deu.pdf
%doc %{_texmfdistdir}/doc/latex/caption/caption-deu.tex
%doc %{_texmfdistdir}/doc/latex/caption/caption-eng.pdf
%doc %{_texmfdistdir}/doc/latex/caption/caption-eng.tex
%doc %{_texmfdistdir}/doc/latex/caption/caption-rus.pdf
%doc %{_texmfdistdir}/doc/latex/caption/caption-rus.tex
%doc %{_texmfdistdir}/doc/latex/caption/caption.pdf
%doc %{_texmfdistdir}/doc/latex/caption/caption2.pdf
%doc %{_texmfdistdir}/doc/latex/caption/caption3.pdf
%doc %{_texmfdistdir}/doc/latex/caption/cat.eps
%doc %{_texmfdistdir}/doc/latex/caption/elephant.eps
%doc %{_texmfdistdir}/doc/latex/caption/ltcaption.pdf
%doc %{_texmfdistdir}/doc/latex/caption/subcaption.pdf
#- source
%doc %{_texmfdistdir}/source/latex/caption/bicaption.dtx
%doc %{_texmfdistdir}/source/latex/caption/caption.dtx
%doc %{_texmfdistdir}/source/latex/caption/caption.ins
%doc %{_texmfdistdir}/source/latex/caption/caption2.dtx
%doc %{_texmfdistdir}/source/latex/caption/caption3.dtx
%doc %{_texmfdistdir}/source/latex/caption/ltcaption.dtx
%doc %{_texmfdistdir}/source/latex/caption/subcaption.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
