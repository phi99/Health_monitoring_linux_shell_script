#*in progress*

test_connectivity() {
  target=$1
  if ping -c 1 -W 3 $target > /dev/null 2>&1; then
    echo "$target Reachable"
  else
    echo "$target Unreachable"
  fi
}

