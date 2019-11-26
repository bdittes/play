workspace(name = "com_bdittes_play")

load("@bazel_tools//tools/build_defs/repo:git.bzl", "new_git_repository")

new_git_repository(
    name = "cpp-httplib",
    tag = "v0.2.5",
    build_file = "BUILD.httplib",
    init_submodules = True,
    remote = "https://github.com/yhirose/cpp-httplib.git",
)

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# abseil-cpp, from absl/absl-hello
http_archive(
  name = "absl",
  urls = ["https://github.com/abseil/abseil-cpp/archive/7c7754fb3ed9ffb57d35fe8658f3ba4d73a31e72.zip"],  # 2019-03-14
  strip_prefix = "abseil-cpp-7c7754fb3ed9ffb57d35fe8658f3ba4d73a31e72",
  sha256 = "71d00d15fe6370220b6685552fb66e5814f4dd2e130f3836fc084c894943753f",
)
