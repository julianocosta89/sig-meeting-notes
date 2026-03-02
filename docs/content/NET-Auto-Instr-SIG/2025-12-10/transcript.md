SIG: .NET Auto-Instr SIG
Date: 2025-12-10
Duration: 14 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 02:43 Hey, Raj, I'm in the pretty noisy place, so if you could drive, it would be great.
**Rajkumar Rangaraj** 02:52 Peter, I joined from a mobile, actually, so I won't be able to share or anything today.
**Piotr Kiełkowicz** 03:09 So, I refer people myself.
Response.
Sorry for the strange… Fine. I'm good background.
Good morning.
Right.
So, let's start from the fill requests.
there is kind of the technical rate of the new SDKs of experience.
And yeah, that's true, important time.
PRs.
One of them is, regularly support for N-Log.
And dig down through all three of them, I think, correlation blue.
Thumbs?
I think it is almost ready to merge. There is only…
However, it's Lucy. I follow the,
you know, providing insurance bubble. So, internship time, It'd be great to review.
I think that sticker… Who provides the bay.
Last update to the tier related to the capturing analytics.
BookNet Framework postdocs.
And with this, we should be able to also make the second chart for preview, and hopefully merge it.
What's it solo?
Access is the pull request.
Right.
No issues.
I think Frisk handled this issue correctly. We need to wait for the response, I will keep it as it is.
without… That's it. So now…
I love that we can.
Advice on the clinical trial?
I have a stereotypical term.
**Igor Kiselev** 07:21 carries, with such type of, issue as that one, we probably should do.
**Piotr Kiełkowicz** 07:29 in NuGet.
**Igor Kiselev** 07:31 add in a GET package some additional validation or compile time that would produce a built error if we detected a downgrading of some packages, because by default, downgrading of packages is a one-level issue.
So, I would probably create a ticket for, an issue for it.
**Piotr Kiełkowicz** 07:52 I'm pretty sure that the customers are not using the NuGet packages. There were no… nobody…
Make a Neroic regret, For us, telling her, so far, nobody was complaining. They were using for the credits.
I'm not against creating this asset improvement, but it will not solve this issue. The customers will probably care for utilizing the packages.
Because…
**Igor Kiselev** 08:30 Okay, maybe I misunderstand it, because I… I read Erasmus comment as, we believe that customer reference both, us and system diagnostics manually.
**Piotr Kiełkowicz** 08:45 Yes.
If the application is referencing or reverse it.
**Igor Kiselev** 08:50 Yes.
**Piotr Kiełkowicz** 08:51 And they look… and the custom… and the same application is not a reference other package.
But the zip file is, let's say, integrated into the
In the runtime by the environmental variables, it will be… it leads to the problems.
If they will utilize our nuggets package.
If you forgot, he upgrades that system diagnosis of that.
**Igor Kiselev** 09:19 It would not upgrade a package for customer if customer reference both us and system diagnostic, diagnostic source at level.
**Piotr Kiełkowicz** 09:29 Directly. Is it really kind of…
Indirect reference, it will be upgraded to our world.
**Igor Kiselev** 09:37 Yes.
**Piotr Kiełkowicz** 09:38 And I've never met the customer who were complying
About these cases, to be honest.
**Igor Kiselev** 09:49 They were always complaining about the.
**Piotr Kiełkowicz** 09:53 Cases when they were using all music files.
**Igor Kiselev** 10:00 Okay.
**Alexey Pukhov** 10:01 Interesting.
**Piotr Kiełkowicz** 10:01 But thank you.
But, but I'm not against… the improvement, guys. That's telling that it will not solve
That it will be probably not solving the issue.
**Igor Kiselev** 10:12 I… because I believe that if customer uses Zip Archive, and he have additional depths, additional depths, it should auto-upgrade. I need to test also a bit more that situation.
Because in the case of ZeeperHive, I do… I… and with addition, this should upgrade assembly into pass-through additional depths.
Probably not, probably I misunderstand something.
**Piotr Kiełkowicz** 10:40 it will be not working. If there is direct reference, ex…
If they are working on older version that does not generate now, They need to…
And if they provide direct reference to diagnostic source, V9, it will be loaded.
With the higher priority than our dependents.
**Igor Kiselev** 11:04 Okay, maybe.
**Piotr Kiełkowicz** 11:05 Negro.
For sure.
**Igor Kiselev** 11:09 Got it. I would… check it, and we're looking through it. Thank you. Okay.
**Alexey Pukhov** 11:15 Yeah, I think if the… hypothetically, if the customer is using… I mean, for example, creating spans themselves.
So they must reference.
A diagnostic library directly.
And then, if they happen to use art as well.
This is… this, I believe, will be the conflict where the version referenced and the customer application will take the priority.
**Piotr Kiełkowicz** 11:40 Eve?
**Alexey Pukhov** 11:41 Maybe not very popular.
**Piotr Kiełkowicz** 11:43 If the customer… if the customer is using…
a referencing diagnostic source directly in the application CS Croil.
Project. Yes? Yes, if they are… if it will be kind of…
In direct dependency through the library, the higher version will win.
**Alexey Pukhov** 12:08 Oh yeah, if it's not a direct dependency, I believe the higher version will take priority. If it's a direct dependency, then the direct dependency will take the priority.
**Piotr Kiełkowicz** 12:19 I don't know how popular that use case, the second one.
**Alexey Pukhov** 12:23 But, hypothetically, it can happen.
**Piotr Kiełkowicz** 12:26 So, I've never met this, the problematic one you are discussing.
**Igor Kiselev** 12:31 What a…
**Alexey Pukhov** 12:32 Just for the record.
**Piotr Kiełkowicz** 12:34 True.
I will check. I think that I can check with Steve, offline if he needs some support few more, or even thousands.
For now, there's an immediate way how to utilize
On configuration 2014, so that's what we need to… And they're not,
Claude.
So, this is a handbook.
No discussions… tomorrow's fine.
Oh, that reference looks fine.
I'm not supposed to be today.
We need to update this program, I think that we are fine.
Do you have any other topics to discuss today, guys?
**Alexey Pukhov** 14:15 I'm good.
**Piotr Kiełkowicz** 14:19 So we were looking for the… issue, or… even better PR with improvement.
But kind of not high priority, in my opinion, at least for me.
Thank you, guys. Have a nice day.
**Alexey Pukhov** 14:46 Bye.
**efshaikh** 14:47 Yankee.
