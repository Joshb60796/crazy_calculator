from pydantic import BaseModel, Field
from typing import Optional
import math

class MemoryState(BaseModel):
    """Represents the current state of calculator memory."""
    value: Optional[float] = Field(default=None, description="The current memory value")

class MemoryManager:
    """Manages calculator memory operations."""
    
    def __init__(self):
        self._memory = MemoryState()
    
    def store(self, value: float) -> None:
        """
        Store a value in memory.
        
        Args:
            value: The value to store in memory
        """
        self._memory.value = value
    
    def recall(self) -> Optional[float]:
        """
        Recall the value from memory.
        
        Returns:
            The value stored in memory, or None if memory is empty
        """
        return self._memory.value
    
    def add(self, value: float) -> None:
        """
        Add a value to the current memory value.
        
        Args:
            value: The value to add to memory
        """
        if self._memory.value is None:
            self._memory.value = value
        else:
            self._memory.value += value
    
    def subtract(self, value: float) -> None:
        """
        Subtract a value from the current memory value.
        
        Args:
            value: The value to subtract from memory
        """
        if self._memory.value is None:
            self._memory.value = -value
        else:
            self._memory.value -= value
    
    def clear(self) -> None:
        """Clear the memory."""
        self._memory.value = None
    
    def get_state(self) -> MemoryState:
        """
        Get the current memory state.
        
        Returns:
            MemoryState object representing current memory
        """
        return self._memory
