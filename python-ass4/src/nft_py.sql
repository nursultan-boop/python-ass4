PGDMP         #            
    z            nft_py    13.8    13.8     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    17477    nft_py    DATABASE     c   CREATE DATABASE nft_py WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';
    DROP DATABASE nft_py;
                postgres    false            �            1259    42306    nft    TABLE     k   CREATE TABLE public.nft (
    adrs character varying NOT NULL,
    meta_data character varying NOT NULL
);
    DROP TABLE public.nft;
       public         heap    postgres    false            �            1259    17494 
   testvalues    TABLE     K   CREATE TABLE public.testvalues (
    randomstring character varying(50)
);
    DROP TABLE public.testvalues;
       public         heap    postgres    false            �            1259    42322    users    TABLE     j   CREATE TABLE public.users (
    login character varying NOT NULL,
    pswrd character varying NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false            �          0    42306    nft 
   TABLE DATA           .   COPY public.nft (adrs, meta_data) FROM stdin;
    public          postgres    false    201   }
       �          0    17494 
   testvalues 
   TABLE DATA           2   COPY public.testvalues (randomstring) FROM stdin;
    public          postgres    false    200   O       �          0    42322    users 
   TABLE DATA           -   COPY public.users (login, pswrd) FROM stdin;
    public          postgres    false    202   �       +           2606    42313    nft nft_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY public.nft
    ADD CONSTRAINT nft_pkey PRIMARY KEY (adrs);
 6   ALTER TABLE ONLY public.nft DROP CONSTRAINT nft_pkey;
       public            postgres    false    201            -           2606    42329    users users_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (login);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    202            �   �  x��Ko�F��ͧ���46�a����66n�`��y��r���IUݤҍn�h�Jݍ����?��Aޜh���4��M9���P�p:���W㴊й)ퟞ�e��2�U��	�P�2�	�h4)����}��	}���f�d�з���� ���9R��`����|LPv�"���Q����ܖ|�|/Ia�7�8�d�i�4��3/��"�H�r8��c��N�:�59�"=�:7��&:� ;�Y���l�E��]��8�*�)��)̔m�n�V*�
�or*f��p��JA�� �+P0�T����V4�gA1}3�P��SN�X�Ō���j�y��V͹:-�2��҂�m`�B�gC|x���㍋�u~���/�=05^B#��!�g X-DUq�×�;�B��[6;���K���X(�/���~��"*|��!vK�1����V��dI
V�h�Vm̓�o+l'U�oNKed��0��7�n��b�<��_D�{O�r:}�4P�4�1�d�[:��p�Ҧ�}�Mf�urkir�q��ϡ���k�]��f��_ͱ��0�E��J_V\��]��N?.>��V��#���2���z���#�5a�尉E��}E8h��sݸ�?|����d�$��,�n���S*�W���ނe1a^��X�e9�hw#-���sJ�:�A�^G����/ײ�o���G��齍2�*��]֨�`ro���v,
�]��7�Fb׆ے�h�`����~�:Ϗ��b��ט���~�8�wM�I�fɢ��F��_��li���tK��]ΥVD�2݇���[m3�	�S"e,�sT/�]k]J{�ћ�j�l}B�0�&����Ʋ��*�ݍߘv�!�4du�	��E��&=yl�])蚿v��r�#I�\���\�ݣ�l�:"g�X\��c���ZJ7���ǻ���6��      �   ;   x�K,NMIK�*K+��K,NOI��(��I\�
y�I�E%%\�99�
��E9)\1z\\\ �7      �   J   x��A
�0�s�%qӘ��K��bi����kk#��{{��dC��B����Y�ڸ��$���,�V:V"����     