{ pkgs ? import <nixpkgs> {} }:
with pkgs;

python3Packages.buildPythonPackage {
  pname = "logtimes";
  version = "0.1.0";
  pyproject = true;


  src = ./.;

  build-system = with python3Packages; [
    hatchling 
  ];

  propagatedBuildInputs = with python3Packages; [
    python-dateutil
  ];
}
