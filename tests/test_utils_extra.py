import unittest

from o3research.core.self_reflection import SelfReflection
from o3research.core.semantic_cache import SemanticCache
from o3research.core.token_optimizer import TokenOptimizer
from o3research.core.few_shot_selector import FewShotSelector


class TestSelfReflectionScore(unittest.TestCase):
    def test_score_below_100(self) -> None:
        text = "x" * 50
        self.assertEqual(SelfReflection().score(text), 3)

    def test_score_between_100_and_200(self) -> None:
        text = "x" * 150
        self.assertEqual(SelfReflection().score(text), 4)

    def test_score_above_200(self) -> None:
        text = "x" * 250
        self.assertEqual(SelfReflection().score(text), 5)


class TestSemanticCache(unittest.TestCase):
    def test_get_unset_returns_none(self) -> None:
        cache = SemanticCache()
        self.assertIsNone(cache.get("missing"))

    def test_set_then_get_round_trip(self) -> None:
        cache = SemanticCache()
        cache.set("a", "b")
        self.assertEqual(cache.get("a"), "b")


class TestTokenOptimizer(unittest.TestCase):
    def test_trim_long_text(self) -> None:
        optimizer = TokenOptimizer(limit=10)
        text = "a" * 20
        self.assertEqual(len(optimizer.trim(text)), 10)

    def test_trim_short_text_unchanged(self) -> None:
        optimizer = TokenOptimizer(limit=10)
        text = "short"
        self.assertEqual(optimizer.trim(text), text)


class TestFewShotSelector(unittest.TestCase):
    def test_select_returns_example(self) -> None:
        selector = FewShotSelector({"topic": "example"})
        self.assertEqual(selector.select("topic"), "example")

    def test_select_unknown_returns_empty_string(self) -> None:
        selector = FewShotSelector({"topic": "example"})
        self.assertEqual(selector.select("other"), "")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
