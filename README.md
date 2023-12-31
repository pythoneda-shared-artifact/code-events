# code-events

Events used to transform artifact events into code.

## How to declare it in your flake

Check the latest tag of the artifact repository: https://github.com/pythoneda-shared-artifact/code-events-artifact/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-shared-artifact-code-events = {
      [optional follows]
      url =
        "github:pythoneda-shared-artifact/oced-events-artifact/[version]?dir=code-events";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [https://nixos/nixpkgs](nixpkgs "nixpkgs") and [https://github.com/numtide/flake-utils](flake-utils "flake-utils").

The Nix flake is under the [https://github.com/pythoneda-shared-artifact/code-events-artifact/tree/main/code-events](code-events "code-events") folder of <https://github.com/pythoneda-shared-artifact/code-events-artifact>.

