%global tl_name caption
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Customising captions in floating environments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/caption
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/caption.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/caption.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/caption.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The caption package provides many ways to customise the captions in
floating environments like figure and table, and cooperates with many
other packages. Facilities include rotating captions, sideways captions,
continued captions (for tables or figures that come in several parts). A
list of compatibility notes, for other packages, is provided in the
documentation. The package also provides the "caption outside float"
facility, in the same way that simpler packages like capt-of do. The
package supersedes caption2.

