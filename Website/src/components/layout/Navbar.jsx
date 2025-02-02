import {
  Box,
  Flex,
  HStack,
  IconButton,
  Button,
  Menu,
  MenuButton,
  MenuList,
  MenuItem,
  useDisclosure,
  useColorModeValue,
  Image,
} from '@chakra-ui/react';
import { HamburgerIcon, CloseIcon } from '@chakra-ui/icons';
import { Link as RouterLink, useLocation } from 'react-router-dom';
import { motion } from 'framer-motion';

const MotionBox = motion(Box);

const NavLink = ({ children, to }) => {
  const location = useLocation();
  const isActive = location.pathname === to;

  return (
    <MotionBox
      whileHover={{ scale: 1.1 }}
      whileTap={{ scale: 0.95 }}
    >
      <Button
        as={RouterLink}
        to={to}
        variant="ghost"
        p={2}
        bg={isActive ? 'whiteAlpha.200' : 'transparent'}
        _hover={{
          bg: 'whiteAlpha.300',
          textDecoration: 'none',
        }}
        position="relative"
        overflow="hidden"
        _after={{
          content: '""',
          position: 'absolute',
          bottom: '0',
          left: '0',
          width: isActive ? '100%' : '0%',
          height: '2px',
          bg: 'blue.400',
          transition: '0.3s',
        }}
        _hover_after={{
          width: '100%',
        }}
      >
        {children}
      </Button>
    </MotionBox>
  );
};

function Navbar() {
  const { isOpen, onToggle } = useDisclosure();
  const bg = useColorModeValue('gray.800', 'gray.900');

  return (
    <Box 
      bg={bg} 
      px={4} 
      position="fixed" 
      w="100%" 
      top="0" 
      zIndex="1000"
      boxShadow="0 2px 10px rgba(0,0,0,0.3)"
      backdropFilter="blur(10px)"
    >
      <Flex h={16} alignItems="center" justifyContent="space-between">
        <IconButton
          size="md"
          icon={isOpen ? <CloseIcon /> : <HamburgerIcon />}
          aria-label="Open Menu"
          display={{ md: 'none' }}
          onClick={onToggle}
        />

        <HStack spacing={8} alignItems="center">
          <Box>
            <Image
              height="40px"
              src="/chess-logo.png" // You'll need to add this image to your public folder
              alt="Chess Logo"
            />
          </Box>
          <HStack as="nav" spacing={4} display={{ base: 'none', md: 'flex' }}>
            <NavLink to="/">Home</NavLink>
            <NavLink to="/import">Import Game</NavLink>
            <NavLink to="/analysis">Analysis</NavLink>
            <NavLink to="/practice">Practice AI</NavLink>
            <NavLink to="/leaderboard">Leaderboard</NavLink>
            <NavLink to="/about">About</NavLink>
            <NavLink to="/contact">Contact</NavLink>
          </HStack>
        </HStack>

        <Box display={{ base: 'none', md: 'block' }}>
          <Button
            as={motion.button}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            colorScheme="blue"
            size="sm"
          >
            Sign In
          </Button>
        </Box>
      </Flex>

      {/* Mobile menu */}
      {isOpen && (
        <Box pb={4} display={{ md: 'none' }}>
          <Stack as="nav" spacing={4}>
            <NavLink to="/">Home</NavLink>
            <NavLink to="/import">Import Game</NavLink>
            <NavLink to="/analysis">Analysis</NavLink>
            <NavLink to="/practice">Practice AI</NavLink>
            <NavLink to="/leaderboard">Leaderboard</NavLink>
            <NavLink to="/about">About</NavLink>
            <NavLink to="/contact">Contact</NavLink>
          </Stack>
        </Box>
      )}
    </Box>
  );
}

export default Navbar; 