import logging 

def load_fasta():
   with open("data_input/input.txt", "r", encoding = "utf8") as file_obj: 
         file = file_obj.read().splitlines()
     
         if not file:
            raise ValueError("File is empty")
 
         dict = {}

         header_found = False

         for i in range(len(file)):
          
          if file[i] == "":
            continue
         
          elif file[i].startswith(">"):
          
           header = file[i][1:]
        
         parts = header.split(maxsplit=1)

         record_id = parts[0]
       
         if len(parts) > 1:
          description = parts[1]
         else:
          description = ""
        
         if record_id in dict:
             logging.warning("Duplicate ID: " + record_id)
             continue

         header_found = True

         sequence = ""

         for j in range(i + 1, len(file)):

            if file[j].startswith(">"):
               break

            if file[j] == "":
               continue
             
            sequence += file[j].upper()

            if sequence == "":
               raise ValueError("header has no sequence")
            
            dict[record_id] = sequence

         #if i + 1 >= len(file) or file[i + 1] == "":
            #raise ValueError("header has no sequence")
        
         #dict[record_id] = file[i+1].upper()

         else:
          if not header_found:
            raise ValueError("Sequence before header")
          
          continue

 return dict

load_fasta()
