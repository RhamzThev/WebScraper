from abc import ABC, abstractmethod


class UI(ABC):
    
    @abstractmethod
    def get_input_file(self): pass
    
    @abstractmethod
    def get_keyword(self): pass
    
    @abstractmethod
    def get_output_folder(self): pass

    @abstractmethod
    def get_pre_summary(self, input, keyword, output): pass

    @abstractmethod
    def get_post_summary(self, input, keyword, output): pass