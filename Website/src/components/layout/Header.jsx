import {
  Box,
  Flex,
  Button,
  Image,
  Menu,
  MenuButton,
  MenuList,
  MenuItem,
  Avatar,
  useColorModeValue,
} from '@chakra-ui/react';
import { Link as RouterLink } from 'react-router-dom';

function Header() {
  const isLoggedIn = false; // Replace with actual auth state
  const bgColor = useColorModeValue('white', 'brand.dark');

  return (
    <Box as="header" bg={bgColor} px={4} py={2} shadow="sm">
      <Flex maxW="1200px" mx="auto" align="center" justify="space-between">
        <Flex align="center">
          <RouterLink to="/">
            <Image h="40px" src="/logo.png" alt="ChessInsights Logo" />
          </RouterLink>
          
          <Flex ml={8} gap={4}>
            <Button as={RouterLink} to="/" variant="ghost">Home</Button>
            <Button as={RouterLink} to="/import" variant="ghost">Import Game</Button>
            <Button as={RouterLink} to="/practice" variant="ghost">Practice with AI</Button>
            <Button as={RouterLink} to="/leaderboard" variant="ghost">Leaderboard</Button>
            <Button as={RouterLink} to="/about" variant="ghost">About</Button>
            <Button as={RouterLink} to="/contact" variant="ghost">Contact</Button>
          </Flex>
        </Flex>

        <Box>
          {isLoggedIn ? (
            <Menu>
              <MenuButton as={Button} variant="ghost">
                <Avatar size="sm" />
              </MenuButton>
              <MenuList>
                <MenuItem>Profile</MenuItem>
                <MenuItem>Settings</MenuItem>
                <MenuItem>Logout</MenuItem>
              </MenuList>
            </Menu>
          ) : (
            <Button colorScheme="blue">Login / Register</Button>
          )}
        </Box>
      </Flex>
    </Box>
  );
}

export default Header; 