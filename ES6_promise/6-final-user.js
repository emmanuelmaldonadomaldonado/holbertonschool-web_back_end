import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName);
  const photoPromise = uploadPhoto(fileName);

  try {
    const [userData, photoData] = await Promise.all([userPromise, photoPromise]);

    return [
      { status: 'fulfilled', value: userData },
      { status: 'fulfilled', value: photoData },
    ];
  } catch (error) {
    return [
      { status: 'rejected', value: error },
    ];
  }
}

export default handleProfileSignup;
