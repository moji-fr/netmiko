from typing import Any, Optional
import re
from netmiko.linux.linux_ssh import LinuxSSH

class TheBastionSSH(LinuxSSH):
    """Netmiko SSH driver for OVH's The Bastion."""
    
    def session_preparation(self) -> None:
        """Handle The Bastion's specific welcome message and prompt."""
        self.ansi_escape_codes = True
        
        self._test_channel_read(pattern=r"Loading\.\.\. \d+ commands and \d+ autocompletion rules loaded\.")
        
        self.prompt_pattern = r"\)> "
        self.set_base_prompt()

    def set_base_prompt(
        self,
        pri_prompt_terminator: str = ">",
        alt_prompt_terminator: str = ">",
        delay_factor: float = 1.0,
        pattern: Optional[str] = None,
    ) -> str:
        """Set the base prompt for The Bastion."""
        if pattern is None:
            pattern = self.prompt_pattern
        return super().set_base_prompt(
            pri_prompt_terminator=pri_prompt_terminator,
            alt_prompt_terminator=alt_prompt_terminator,
            delay_factor=delay_factor,
            pattern=pattern,
        )

    def find_prompt(
        self, delay_factor: float = 1.0, pattern: Optional[str] = None
    ) -> str:
        """Find the current prompt using The Bastion's specific pattern."""
        if pattern is None:
            pattern = self.prompt_pattern
        return super().find_prompt(delay_factor=delay_factor, pattern=pattern)
