from cli_calculator.memory_manager import MemoryManager, MemoryState
import pytest

def test_memory_manager_initialization():
    """Test that memory manager initializes correctly."""
    mm = MemoryManager()
    assert mm.get_state().value is None

def test_memory_store():
    """Test storing a value in memory."""
    mm = MemoryManager()
    mm.store(42.0)
    assert mm.get_state().value == 42.0

def test_memory_recall():
    """Test recalling a value from memory."""
    mm = MemoryManager()
    mm.store(10.5)
    assert mm.recall() == 10.5

def test_memory_recall_empty():
    """Test recalling from empty memory."""
    mm = MemoryManager()
    assert mm.recall() is None

def test_memory_add():
    """Test adding to memory."""
    mm = MemoryManager()
    mm.store(5.0)
    mm.add(3.0)
    assert mm.get_state().value == 8.0

def test_memory_add_to_empty():
    """Test adding to empty memory."""
    mm = MemoryManager()
    mm.add(7.0)
    assert mm.get_state().value == 7.0

def test_memory_subtract():
    """Test subtracting from memory."""
    mm = MemoryManager()
    mm.store(10.0)
    mm.subtract(3.0)
    assert mm.get_state().value == 7.0

def test_memory_subtract_from_empty():
    """Test subtracting from empty memory."""
    mm = MemoryManager()
    mm.subtract(5.0)
    assert mm.get_state().value == -5.0

def test_memory_clear():
    """Test clearing memory."""
    mm = MemoryManager()
    mm.store(42.0)
    mm.clear()
    assert mm.get_state().value is None

def test_memory_clear_empty():
    """Test clearing already empty memory."""
    mm = MemoryManager()
    mm.clear()
    assert mm.get_state().value is None

def test_memory_state_serialization():
    """Test that MemoryState can be properly serialized."""
    mm = MemoryManager()
    mm.store(3.14)
    state = mm.get_state()
    assert isinstance(state, MemoryState)
    assert state.value == 3.14
