# Data Structure/Library	         Mutable	                                     Immutable
# String	                ❌ (Cannot be modified in place)	                       ✅ (Immutable by nature)
# Tuple	                    ❌ (Cannot be modified in place)	                       ✅ (Immutable by nature)
# List	                    ✅ (Can be modified in place)	                           ❌ (Mutable by nature)
# Set                     	✅ (Set is mutable, elements must be immutable)        	   ❌ (Mutable by nature)
# Dictionary	            ✅ (Can be modified in place; keys must be immutable)      ❌ (Mutable by nature)
# Pandas DataFrame	        ✅ (Can be modified in place)	                           ❌ (Mutable by nature)
# Pandas Series	            ✅ (Values can be changed)                                 ✅ (Length is immutable)
# NumPy Array              	✅ (Can be modified in place)	                           ❌ (Mutable by nature)
# Matplotlib Objects	    ✅ (Can be modified in place)                              ❌ (Mutable by nature)
# Key Notes:
# Strings and Tuples are inherently immutable, meaning their content cannot be altered once created.
# Lists, Sets, and Dictionaries are mutable, allowing modification of their contents.
# Sets and Dictionaries require their elements or keys to be immutable.
# Pandas DataFrame and Series allow modifications, but a Series has an immutable length.
# NumPy Arrays and Matplotlib Objects are mutable, permitting changes to their state.