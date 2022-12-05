import json
import shutil
from pathlib import Path

from byu_pytest_utils import test_files, check_io, max_score

original_inventory = test_files / "original_inventory.json"


def copy_inventory(name) -> Path:
    target = name + ".inventory.json"
    return shutil.copy(original_inventory, target)


def assert_inventory(observed, expected):
    with open(observed) as f:
        obs = json.load(f)
    with open(expected) as f:
        exp = json.load(f)
    assert obs == exp


# Quit
@max_score(5)
def test_shopping_cart_quit():
    inventory = copy_inventory('quit')
    check_io(
        test_files / "quit.txt",
        "shopping_cart.py", inventory
    )
    assert_inventory(inventory, test_files / "quit.expected.json")


# Add item and quit
@max_score(5)
def test_shopping_cart_add_item():
    inventory = copy_inventory('add_item')
    check_io(
        test_files / "add_item.txt",
        "shopping_cart.py", inventory
    )
    assert_inventory(inventory, test_files / "add_item.expected.json")


# No query match
@max_score(5)
def test_shopping_cart_no_match():
    inventory = copy_inventory('no_match')
    check_io(
        test_files / "no_match.txt",
        "shopping_cart.py", inventory
    )
    assert_inventory(inventory, test_files / "no_match.expected.json")


@max_score(5)
def test_shopping_cart_all_match():
    inventory = copy_inventory('all_match')
    check_io(
        test_files / "all_match.txt",
        "shopping_cart.py", inventory
    )
    assert_inventory(inventory, test_files / "all_match.expected.json")


# Add multiple items and quit
@max_score(5)
def test_shopping_cart_add_multiple_items():
    inventory = copy_inventory('add_mult_items')
    check_io(
        test_files / "add_mult_items.txt",
        "shopping_cart.py", inventory
    )
    assert_inventory(inventory, test_files / "add_mult_items.expected.json")


# Add multiple items and view cart
@max_score(5)
def test_shopping_cart_add_multiple_view():
    inventory = copy_inventory('add_mult_view')
    check_io(
        test_files / "add_mult_view.txt",
        "shopping_cart.py", inventory
    )
    assert_inventory(inventory, test_files / "add_mult_view.expected.json")


# View empty cart
@max_score(5)
def test_shopping_cart_view_empty():
    inventory = copy_inventory('view_empty')
    check_io(
        test_files / "view_empty.txt",
        "shopping_cart.py", inventory
    )
    assert_inventory(inventory, test_files / "view_empty.expected.json")


# Add item and checkout
@max_score(10)
def test_shopping_cart_single_checkout():
    inventory = copy_inventory('single_checkout')
    check_io(
        test_files / "single_checkout.txt",
        "shopping_cart.py", inventory
    )
    assert_inventory(inventory, test_files / "single_checkout.expected.json")


# Repeated items
@max_score(10)
def test_shopping_cart_repeat_item_checkout():
    inventory = copy_inventory('repeat_item_checkout')
    check_io(
        test_files / "repeat_item_checkout.txt",
        "shopping_cart.py", inventory
    )
    assert_inventory(inventory, test_files / "repeat_item_checkout.expected.json")


# Checkout - not confirmed
@max_score(10)
def test_shopping_cart_checkout_not_confirmed():
    inventory = copy_inventory('checkout_not_confirmed')
    check_io(
        test_files / "checkout_not_confirmed.txt",
        "shopping_cart.py", inventory
    )
    assert_inventory(inventory, test_files / "checkout_not_confirmed.expected.json")


# Add multiple items and checkout
@max_score(10)
def test_shopping_cart_multi_checkout():
    inventory = copy_inventory('multi_checkout')
    check_io(
        test_files / "multi_checkout.txt",
        "shopping_cart.py", inventory
    )
    assert_inventory(inventory, test_files / "multi_checkout.expected.json")


# Add-checkout cycle twice
@max_score(10)
def test_shopping_cart_repeat_checkout():
    inventory = copy_inventory('repeat_checkout')
    check_io(
        test_files / "repeat_checkout.txt",
        "shopping_cart.py", inventory
    )
    assert_inventory(inventory, test_files / "repeat_checkout.expected.json")


# Add no items and checkout
@max_score(5)
def test_shopping_cart_empty_checkout():
    inventory = copy_inventory('empty_checkout')
    check_io(
        test_files / "empty_checkout.txt",
        "shopping_cart.py", inventory
    )
    assert_inventory(inventory, test_files / "empty_checkout.expected.json")


# Run out of items
@max_score(10)
def test_shopping_cart_exhaust_checkout():
    inventory = copy_inventory('exhaust_checkout')
    check_io(
        test_files / "exhaust_checkout.txt",
        "shopping_cart.py", inventory
    )
    assert_inventory(inventory, test_files / "exhaust_checkout.expected.json")
