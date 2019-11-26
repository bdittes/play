#include <iostream>

#include "absl/strings/str_cat.h"
#include "absl/time/clock.h"
#include "absl/time/time.h"
#include "httplib.h"

int main() {
  using namespace httplib;

  Server svr;

  svr.Get("/hi", [](const Request &req, Response &res) {
    res.set_content(
        absl::StrCat("Hello World! ", absl::FormatTime(absl::Now())),
        "text/plain");
  });

  svr.Get(R"(/numbers/(\d+))", [&](const Request &req, Response &res) {
    auto numbers = req.matches[1];
    res.set_content(numbers, "text/plain");
  });

  svr.Get("/stop", [&](const Request &req, Response &res) { svr.stop(); });

  std::cout << "Started." << std::endl;
  svr.listen("localhost", 1234);
}
