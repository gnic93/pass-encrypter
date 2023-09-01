import os
import utils


def main():
    print('💡 Para contraseñas más fuertes considere una longitud más amplia\n')
    
    max_length: int = 128
    while True:
        try:
            length = int(input('Ingrese longitud de bytes: '))
            if length < 8 or length > max_length:
                raise ValueError(f"La longitud debe estar entre 8 y {max_length}.")
            break
        except ValueError as error:
            print(f"{error}")

    password: str = utils.generate_password(length)
    
    print('\n')
    print('🔒 Contraseña generada con éxito')

    while True:
        save_option = input("¿Deseas guardar esta contraseña en un archivo cifrado? (s/n): ")
        filename: str = './files/pass.txt'

        if save_option.lower() == 's':
            if not os.path.exists(filename):
                utils.save_encrypted_password(password, filename)
                print("Contraseña guardada en el archivo cifrado:", filename)
            else:
                filename = input('Ingrese una ruta donde guardar el archivo: ')
                utils.save_encrypted_password(password, filename)
                print("Contraseña guardada en el archivo cifrado:", filename)
                
        key_filename: str = './files/clave.key'

        if not os.path.exists(key_filename):
            key: bytes = utils.key
            utils.save_key_to_file(key, key_filename)
            print('Llave guardada con éxito en:', key_filename)
        else:
            key_filename = input('Ingrese una ruta donde guardar su llave: ')
            key: bytes = utils.key
            utils.save_key_to_file(key, key_filename)
            print('Llave guardada con éxito en:', key_filename)

        break


if __name__ == '__main__':
    main()
