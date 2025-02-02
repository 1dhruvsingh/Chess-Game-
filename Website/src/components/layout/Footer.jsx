import { Box, Container, SimpleGrid, Stack, Text, Link } from '@chakra-ui/react';
import { Link as RouterLink } from 'react-router-dom';

function Footer() {
  return (
    <Box bg="brand.dark" color="white" py={10}>
      <Container maxW="1200px">
        <SimpleGrid columns={{ base: 1, md: 4 }} spacing={8}>
          <Stack spacing={6}>
            <Text fontSize="lg" fontWeight="bold">Quick Links</Text>
            <Link as={RouterLink} to="/">Home</Link>
            <Link as={RouterLink} to="/import">Import Game</Link>
            <Link as={RouterLink} to="/practice">Practice with AI</Link>
            <Link as={RouterLink} to="/leaderboard">Leaderboard</Link>
          </Stack>
          
          <Stack spacing={6}>
            <Text fontSize="lg" fontWeight="bold">About</Text>
            <Link as={RouterLink} to="/about">About Us</Link>
            <Link as={RouterLink} to="/contact">Contact</Link>
          </Stack>
          
          <Stack spacing={6}>
            <Text fontSize="lg" fontWeight="bold">Legal</Text>
            <Link href="#">Privacy Policy</Link>
            <Link href="#">Terms of Service</Link>
          </Stack>
          
          <Stack spacing={6}>
            <Text fontSize="lg" fontWeight="bold">Follow Us</Text>
            <Link href="#" isExternal>Twitter</Link>
            <Link href="#" isExternal>Facebook</Link>
            <Link href="#" isExternal>Instagram</Link>
          </Stack>
        </SimpleGrid>
        
        <Text mt={10} textAlign="center">
          © {new Date().getFullYear()} ChessInsights. All rights reserved.
        </Text>
      </Container>
    </Box>
  );
}

export default Footer; 