# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  channel = "stable-23.11"; # or "unstable"
  packages = [
    pkgs.python310Full
    pkgs.python310Packages.django
    pkgs.python310Packages.scikit-learn
  ];
  env = {};
  idx = {
    extensions = [];
    previews = {
      enable = true;
      previews = {};
    };
    workspace = {
      onCreate = {
        default.openFiles = [ ".idx/dev.nix" "README.md" ];
      };
      onStart = {};
    };
  };
}