class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "1#"
        else:
            string = ''
            for i, word in enumerate(strs):
                string = string + word.encode().hex()
                if i < len(strs)-1:
                    string = string + '##'
            return string



    def decode(self, s: str) -> List[str]:
        if s == "1#":
            return [] 
        else:
            words = s.split("##")
            for i, word in enumerate(words):
                words[i] = bytes.fromhex(word).decode()
            return words
