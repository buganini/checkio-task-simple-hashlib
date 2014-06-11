"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ['welcome to pycon', 'sha224'],
            "answer": 'f0ac92efb1ff56b9be0e6da46c8ae1a8d4ae398b089c9b9eaea41269'
        },
        {
            "input": ['welcome to pycon', 'sha256'],
            "answer": 'a555343a86902bf0950f7668a96b8ed718646dbb5f896a2dd09ea0a88f3c00b4'
        },
        {
            "input": ['welcome to pycon', 'sha512'],
            "answer": '91ad76b2163a60a5fa7884483d0f706ac4a252ac5a2e7137600bae99742f3c7cabe0870e7d02cd2cf8f21f3a313c7b45d127dcbae45f192d05ad146344774d6c'
        },
        {
            "input": ['welcome to pycon', 'md5'],
            "answer": '5cca7176c3e14742f117b8e85a1cb262'
        },
        {
            "input": ['welcome to pycon', 'sha1'],
            "answer": '4a14e2da8444f0c05d3f80f4209c1e2f983a83e1'
        },
        {
            "input": ['welcome to pycon', 'sha384'],
            "answer": '0a67310f6eaf6adb5fb6f4c679aedce3716c6d1528a201189c55f631b9656c69f68899dca4699ef44d74a238bd7106e1'
        },

    ],
    "Edge": [
        {
            "input": ['', 'sha1'],
            "answer": 'da39a3ee5e6b4b0d3255bfef95601890afd80709'
        },
        {
            "input": ['', 'sha384'],
            "answer": '38b060a751ac96384cd9327eb1b1e36a21fdb71114be07434c0cc7bf63f6e1da274edebfe76f65fbd51ad2f14898b95b'
        },
        {
            "input": ['', 'md5'],
            "answer": 'd41d8cd98f00b204e9800998ecf8427e'
        },
        {
            "input": ['', 'sha224'],
            "answer": 'd14a028c2a3a2bc9476102bb288234c415a2b01f828ea62ac5b3e42f'
        },
        {
            "input": ['', 'sha512'],
            "answer": 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'
        },
        {
            "input": ['', 'sha256'],
            "answer": 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        },
        {
            "input": [
                'mQDGDbmVYsBXLAqWTzOKtftpsDKaBvbCMjdKiLIbtGmpBvVziHCMxfWKyVxqRrVuZGwrZRUNjQvQcsikWTALjltLdhMeKAmUlKzvCeYDakRXDrCPJfnmwhOcmkcWEHEagnuymeuRvHjKIuECIkQxCHvoZgvknDGSAEGstnVwQXeEgwZmxUvjsKMePcPxHhDHSeEdwtHkQYAlldLAkcvfYzWZnYFVrLhhANPiloHQqNKaVBjQtOxTeGQJACRcCPkeiOEpdLjAsNkXBueGhtvdyZIPlKXqLhnVvubCkfmorpeRlxNUzhEiKwdVjvGmMdDYzgyypjxISCUPPkmpkESyacvLNUZnwpQbtLDMtbpsrvALTiCXPgnJPYUMrnJJJrQgjjaOawNnVTThxbUoabvpWEATWCLDnizzdqEHNoAMGSSDeUpHjXhFcIybfSWphYMVMPDDqgDQSEewLZlaeOhfVjEKanoTcAUtWHQofUfgsknJLmTJpJxuMsfmZdfOfKiYoCrqMMsfpqRWvWzayHYnTDuqIGmdYpdfiiEqmKgmzXVbncIVZlFbuVFHuXyUcuQIDbFPfzwWmghLVWKmwRFGOLVGXfEvPeYXesaACSBfGdwNYuuBwYBRQckBdcmHvESNzYUzwVwAbsGFGJDLYZbVBIGWxiNrmOajNBsnaCWdmOLVBCmZmdWuLRhEjQeGSVqGGusfJnsyyhBwLJsbTBckyyWxVAHCrJVFMneBYeGorKFkeomECyTRPvzvrIEgTVpMoUkmsTyjanETbNULLmeErYThnipnvzuQGWAKzDyDVlJioKehiQKBXBeYSVQrtPdIZKNBQDPYEwueqbyoEEDrIbxqFZyszhLrMwUyETqaQMvpPMVxsYHEQagjLWAYQofurqQIIXqqWuKuxRTFWWifEnqcyvjPiNkdiGsBBbUETOGgtJmkukjIjWepOcFTFHXrdYcvIQZwfUiFWxfapFBQExbFOyfZFQZIKKfODTsJmUQazRaZFBkPgLeZiUlaAhFh',
                'sha1'],
            "answer": 'ccabefdd9e437c70e0c9a8de6cd7f9239c4eb491'
        },
        {
            "input": [
                'xvduUsVcoUSqmhjuEKTlatGhbLOfjLNYlwYdkACNJGkOzdyhvGADCSWJwHBGSVlZSAlmQBAoxOMSfbrPFUrobYLLxpDLZiROeghFrfZEqTjGRHAaRBQmVhTIECyWbSjbIyOPOzcrhoXkPYrOFvdtcmhuoHuUlRLJiQDWiezKATGezXcHmNWQHjXgNxFHFWYqmWwhPsvHGpfHCYseSuCUEucZdOZghqneImvqzJdtNlSYJmIydWLHwjOLpqjvwYYyZRdcWVIQsPXtRTHWLUxVXcFSZoehECqMaeSarOonfhNFLzcSBIYPztpKdDMFeshQagdnuaAFcRJQuTTqAtkwmTYxnRuNMxcRcbwCTBRSENDDacJVJxBgvixgWbEYvunWODPCOKbyYvlLZGkDKtuMwffNXTJkcIMSzMyAWSnbYWJkCYABQkXTHSWXfiIcUDToRqgptVlNnFRlatueJsPxrNMjKsMlhngyKPxbkViYPIRdlxXKWZpqNdBTFYHsXrnvanXdZkYycYJJAaWJgdKJtnXlnyPdwrdewfnTHfdcbYUBaNAptKpqovzPodbFTTUzmvGejYPjxucPcDKzAKMSMoOsZQyIxbDJeLtCtmbiSiYMQjqmGprrjWtNlcYEpCkAhvZRDoSMJNwlzqdFpxCIyakEWNPTGRLaBvSkjBfEaMteFhuLqilhkIlTpfEehAnIpFkXlmjnlICooLPutdHXLpAyGInQtrtpBePBcPldtOffcGjvbnQgyfduigSZISAKLBKgeNLFvtZqNvWSYITnikNtnpiBBXBkYozzuYJLrkqtmYEZuTMIrclSGItYzrmmWOdoODuAMnxtZdbZWjInarNbqmOFFSmtDkamtSnTTGETppIkFCdHxZGMbqquJRxNviSiMbmbGBMjNbgVhNnMgtGYsAKaVYTkvwQXwoxkFypuEALsMdpQCnAvDsxHEqoHPqtdOIrHZqrPsaYOSMNCyGXycJlhMyPcjJbQpPDMTanfgxbdHEkakChTXFrHRwEx',
                'sha384'],
            "answer": '06b23d25c7d9f330378baf7fd6374ba671577ef3858ffd17bf5de80807e7e452eb3c055a3f4f5006dc7379911ed9b505'
        },
        {
            "input": [
                'kzrUUKtEsCdRuYnyOfigDpUrYnMPdKoUCpZoVEfwweUZHQSCrobEKNoenShYSPhWIhZWQjSvVFLaESrqcufFRiHFBVePSvSQygnedyTidPovApinWcqTGxicsrdnHPpmJTyokFlxaLwuyBTomuAYnFRdRXHYAluTUVHuKIWqOnTBkcYzuehyIRYLtXfEiCSTuexZQZMdXYMRCbMrWypxUTYswqHvrrpvCqWykOuJFduYdbsGqbfZWdXCtnWUxspPvIdrlGZxhyBHJHVzSOOoRiGiRhMSaRxdEVktwywJGsBsQRKcqlmKKpCleqfLQxOQuSYthQtGmBRKfwZrOxYFBYLPrbwEmvSqpZbXbYEWzKhdaOBNHhFLTRnXdJahIeRByrHajzegyMUmXRpgvJPFbxhREBNplNCEeIdmaTjJCrkELaWTUiHVbpasTxniyPEypZaHszuSUWBGgfjGzYfMRVursbTxGejGgvYhnnoKQZnISfVHkdYXqTRrFxWVyAWrHCpOeVSsSMAsQrlaJjRzldwgoaHUQaqyhfTPmRZkHngnkvvIJFTHUiDfZZUGzJIlFaAwiLTjaKSOEYSypkVhpqyvtOXulLrJMJEbKggMCuclojpYUjimpPfbDujpkFUSOvYnMWuNACjiWEpPMjKhLCnfCyUfjBMYoKRdRXrDbofoMglehdtkSHIHrEPyLaYowpqIrpWvUfILfpbAmkCHzGUjuajpXdQnhaDepNOgdtTPOAwzJdYncJaheRyetgjBCnVLxiFbMIeDmJLjEKWmyuTVjpFrSpkLntjNWSupPMwnrRqNqRXnPVopoTQuAIUItXxPxDmykxMRThMGKuacRfVFfxpoNnHCaiPEztAfFWbCapWPXetxaxbOaQoKksHQrNYngqxiMwrBQOdtrczDtCXMARiXOtcagmrDqkWKcKrfYmcIcYYOzNhiLqNZoBmGMEpNrcrbTaqihDcVtGXFsXhmOJKXzmkfljaRuUXyfPaguoiDqAnjIaeCXBSOqmrG',
                'md5'],
            "answer": '9b34e286bfb083271de2d1e99346436d'
        },
        {
            "input": [
                'ZgnBZVkeHLWMmShWyFUClKpcaVFtGYlpZlWlngIbPqtNMXUtxvexCrerOemFcvFoVZfKiScumamUNLOOEtxgKRyPKEvfpIKXFzpoJuzVerSFoMSYRkixzwNbKPwxgaaPuxNouwbYCAiLjdLACRgYvMculgJcOPRAVQdEGcTXjDfsiIISchkMRqXYYHfhRQaDOvmknRfhPQFmvyUpXOEOmBdWitVkketKBetXXNDwkrgvwdMOAvpwIXKuDIIILhhtjGHzFXMQEgxHNcZshTBUDAqQAfwDtUhZFfKvJJvcwbBqiaqmfLZECVtUZgtNpTNhpJFlKjKPMdCPbrOGadoaNfiiqHrxUKiDJfBdYGQQBzlJoHNxKRSRlosKRZLUXRVFdRZjuTNJiRQDcjXpcdZGXDwsKdBiVEkwWxjIeZODVWCJtfFzWRGXrkIwnMUmxSzqAmKklAvVjwuiydAuMaIREIeFBfMoMLvOYDufKwuznRbSgQFlRMcXHvKbspkCaVtKDsEgjlhrgDLeyRANjGXuiiRcNDtFJaLzpuNXTsaMORnHwTouWHObNexCUzOhRhRDOBxPdfSjAiCkZDDSMhnhmldbqsNnOsTjFRJnWmwaKNubUZloEPNMgNzxZxuWxNcLleEPDqIyyVLguHYrmJLUXLOHxhaKYQzrEGEvpWMeYpWDfvhfjOYvZrDcFsLNABRnkvcmBbJHdfIFyYFODjezfirYgcbaqtjYIZZhbkoBJLagdWugDLhsnnsDpEVbXsWUmLRXzgwSSEijmCldKxUFxlTMCXOOhWtARqgGNUrPVgdAgJkWSExgCjwaUNRRnGVYDwzhaEXHZagYJxfcAEDRBsSBHqUYaKUSTBcayePxJjcAayJXhahBFOOWwoKanvDlpNQlNDOCWoSJboIWFedIfnwSkKOjRbbaFsACkIldNVUdfazcIFFyrJcpRosgMiSkxCoGEQovagzIXUFyNmIRrQfYkhPwLVvfxzTRcVsoFutfLgLQXeDniSgIhxqXkFup',
                'sha224'],
            "answer": 'd584ab6eb0f671a37b76fba257de870655aa18846ae50a6f357613e7'
        },
        {
            "input": [
                'aCsfqvcIcAeNkoWCEiiecEQBiERugDNTZfbzddVjOGUaUeiYCuHkbRLiTBjXjQeynYhiveVphvvhYrdctvXggRxktOxsgSSxbeLPjdjmsjjEsDGpvQKkvxbtwOnOyECHPwEsgNCizAmHgLlQYSzAkGMLROqpsmuQsaEPxRQGuGoDUwFDLUnpYTHkgVgZMhKWpbKdXAAcOGtsBRUGntdzHmFbbxYXmjHafUWfTQajXzLFbfNxeWxihthgNFATeVojfakfnvGjsHhHvmPqlRbnYMQVVFyXkkkAYEDxHQPXmRryQVZjEPcUHRrNNFdZzpIjycAKwsGMZKRCMUzLijhtoDgFvOIKEfJaGPDkoATXVorCvAwdQmsToLatlBJpsHcStCODEtEEubvAtqphZoPYRPIkLYLILSJqucHKKsmRdaKFJBLXRRcneTUqbBVIhxsuYzBdxzyIheZEiKxXRzXCIwUeBfFBVtcamAyzdKsceoXkZQQWChloEOPlRIUMwDtQVRBvMOjhzCFzLUpKbjCidRHloSwnqyaNPmaLNyjcRTdqajLsKmYxrGAhRloXwRiKcdxAjSZRiHjClBOqguHUDJDNaEgoZMgHAgnbqqAFpMgITFSPprMPoTsTRZvSkUOFLORLTyjcjtAKUKZHhwxyGhyDPsyiszjasYhJAOyzXJbeZEiyPrTkZyudzWLvcbIxcKdqfmzMWlQsiMfcfnUuQtxrryWkDGQxWetcbvtcmxYMmRFszjhCVKzbGEYScdbzwnFoRvPCdiMrqFylkeuzzmxjcIfisHdrxnhARmotTcmnqYLlvGOyxMPcYHyHtuCXhXBbcBwOpCbDOQrACdNqvojBEEVkQmMgVzxAdThtJtAvMFJPKiaffvwKrPJwgpZUvXIeVXpYgMKIvjWwZquTYTfyMgBlkKEFANpDoUFoagdaFFPxKQxaKdsrOtbzGONpgULOlrpapfvWaDhdLpCADehzsPTpAqetdVGdVyJCSbaMQlbLHdRzbOOKgQcEZQmx',
                'sha512'],
            "answer": '642cddde8a77cee7773a5d86cc4d045e1d9b1050759e8d47061d7e5d54fdc13cfcbd74f19862fa6e046cf06171181f086833f03de1bd34e76a315d520bf40e0c'
        },
        {
            "input": [
                'miRwtxTgzRibfYfndBJCeUXzLDQwPiAmmYqLVoNvuGGbBBIFWckJhHooUhcSKFaUFcQlBVKmAhvGtBDPaSLZRbHeFqamabyrseWjjeOpzivATofIOnFrFAHCTYTVfzOWvDvUOqBCtLURbdzQMKfDDHmLfDOowRMAWqVHIoquGFKMXBVnAjHCvFxbpGFbeTipiCVsBNmpuHEFEixwEUibhDMMKwJlpMWKYKoFDFIStFYTIHNQFdLspPXvQjyWLLBYkAIMRsOmmckgZcRAnMdMvajGIbkaEQqskTLfNlHVryRsPtAhuaAHCoIpsjpkRaOdjSOmpNbUwKtkMdVHGWZSOWmTqMPanUuhxVLyQKDkseFURbgcNIqTzMsubCiHhvqrFkzExYHeaqIXzXlHOEFPqWmcKpUjklwLkJbrSQMbzcRSdgKjPTOYdXXrVlVKhNrMIWPKltaQXtoHFwzznSrWZOzkcmKRBfgeoLxuvAuxAEStbphGYGMQBGojQJYioUyxWyvtDSponYJJFbfEugmRTxmOYBjogZytfLQMIRUfbyhAdaaPiXHfpyxZAsDIwOZusljYxDnEuVNcOoqffKfuXOqWkFRIYFluvOnuXIsobCJeAANgCRtonaocXdITmBqVsoddmREhAVTGqAoccyfXGsMDwuLElsbidFQAsLQTnGLfvJfGayDvktpxSiHcANmJxaGBwuzRSXFWmJPBcgdLPdTpxamNgfIjmAosKhGoGxZiftrtOmsQmXatvdRHdCRIyQLfJGZKaCANyscKBqMjaCxSGtlNHfdfxXZaAKYaexXIfhxfLPvQwUBVaqGoCGaITepXAuWAtEDjocJpzXuqkGujybtaVDdaKhvSHbHniVPySjcRZpHuxwohxkQQPIGMIrWSJmSBJmRmUMGilRdCtYwMrpHHkUymXcBTWPElDUuFtkuPtqOPnRzpBpGncPhQImijyqfNrOxHFXsMaKgiQsMgLEOwsdLykVdYtLrXBlIjEKYtaWxtLFMhCvfLfHlv',
                'sha256'],
            "answer": '41373276ad7e6bc8816bda9453c27d47fa98e4a0d2331234cf797c46d3b23440'
        },
    ],
    "Extra": [
        {
            "input": ['密码', 'sha512'],
            "answer": '3ddc7f603e4311ffe52e6ab75c29cf8bc8634449a832b7896ba5c10b228bfd01b6e9d41bc7bc639e63db8f7141ddcb2d9751b673219dd5ffff5088c411b25690'
        },
        {
            "input": ['密码', 'sha384'],
            "answer": '73d9b521d2d3426d0de2b945b4f98e2640beac8e7e8b5dfe43a720bcbb33f0cc1baf2fbad8b97ac9273ee0bf6543098a'
        },
        {
            "input": ['密码', 'sha1'],
            "answer": 'c839a8ff17885af0b098662ccc3ac5e3111b3b3b'
        },

        {
            "input": ['Пароль', 'sha224'],
            "answer": '6102a4a0a632f30c3f7d0fa2da3958da2ca4b09478bbc01a14928447'
        },
        {
            "input": ['Пароль', 'sha256'],
            "answer": 'cb1a2074b3a027ffa7d7d9c54682c3835fffc7f6d620d8a38532f075cc2f17a0'
        },
        {
            "input": ['Пароль', 'md5'],
            "answer": '5ebe553e01799a927b1d045924bbd4fd'
        },
    ]

}
