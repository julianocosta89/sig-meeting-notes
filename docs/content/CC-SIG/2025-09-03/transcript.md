SIG: C/C++ SIG
Date: 2025-09-03
Duration: 18 minutes
============================================================

## Zoom Recording Transcript

**Ehsan** 01:05 Hi, everyone.
**malff** 01:07 Hi, everyone.
**Nikhil Bhatia** 01:10 Hi, everyone.
**malff** 01:28 Lalit has a time conflict, so he cannot attend, Let's wait to see if Tom and Doug can join as well.
And we also need to do that short meeting, because I have another type conflict coming on, so… Issan, Nikhil, or Raphael, do you have any things you want to discuss in particular?
**Nikhil Bhatia** 02:07 Yeah, actually, I had, one thing to discuss, regarding my PR.
So, actually, Ovent is reviewing my PR, and can you hear me?
**malff** 02:27 Barely. I'm trying to… to fix that.
**Nikhil Bhatia** 02:31 Can you hear me now?
**malff** 02:32 Oh, yes, much better, thanks.
**Nikhil Bhatia** 02:35 So, actually, Ovent was, debugging my PR, so, he suggested a couple of changes, but, Can you go in… the resource detection.
**malff** 02:56 Sorry, which one? The resource detector, I'm assuming?
**Nikhil Bhatia** 02:59 Yeah.
**malff** 03:03 Okay.
**Nikhil Bhatia** 03:04 And So, actually, he asked me to… keep it for… in Windows. He asked me to do, like, for Unicode and non-Unicode, so for both the setups, he was asking me to keep get command line… to use get command line A.
Like, it is for older Windows versions. Actually, the newer Windows versions all support, Unicode.
Actually, I shared a link of Microsoft Docs. Can you open it?
**malff** 03:41 This one?
**Nikhil Bhatia** 03:42 Yep.
Actually, there is… there are some, security remarks regarding this, the use of this function, yeah.
Here.
So, it is suggested that, we use get command line W only, so I was, like, confused that… Oh.
What to do now?
**malff** 04:08 Okay. I don't have enough context, so I will need to take a look at the PR and Owen's comments, and I will try to provide comments there.
**Nikhil Bhatia** 04:19 Yeah, sure, thanks.
**malff** 04:21 Okay.
Let me take a note of that.
Okay.
Nikhil, if I remember correctly, last time you had a question on an issue, so, the comments, have you seen them?
**Nikhil Bhatia** 05:10 Yeah, I saw those comments.
Oh, my God.
**malff** 05:14 Good. I also read the semantic convention for that.
Okay, good.
Okay, so it looks like… Tom and Doug, Maybe it will not be there, so we can… we can start then.
I don't… So, I took a look quickly at things which have been moving upstream.
The only thing I noticed is there's a new release of open intermediary Proto.
So, to adjust to that, we will need to, basically update the third-party dependencies and make sure to use third-party or OpenTelementary Portal when building.
from what I've seen, that should not affect anything, because it's only, adding new… new things for profiles, which we don't use yet, and the other signals are unchanged. So, there should be just a matter of adjusting the makefiles, but no impact in the code.
And apart from that, we recently upgraded on the new semantic conventions, so we are up to date there, and likewise, up to date with the tooling with Weaver, so everything is fine.
I don't have any specific topics to discuss. One thing, we noticed is… the integration with Copilot is not working so much, especially, in case of comments… So… easy… the easy CLE check is… is not working.
So if you have a PR, and if Copilot is trying to make comments.
Just don't accept the comment as is, because it's, It's causing issues, so we need to see how to resolve that.
Just something to be aware of.
This should be working, but it's not.
So it will block the merge.
So, like this, if Copilot has some two gesture changes, just don't… Commit as is.
Boom.
Unless there are some specific topics, we can… I'll just go through issues and PRs now.
For new issues, so this, this just came up, it's, it's not an issue, I will reply and close it.
This, someone is upgrading from an old release and saw some changes in the build.
And I think I went as, replied with more details there.
So, it might not be… You know, to… I need to take a look, but it's probably not an issue in the code, it's something to clarify.
This one, I've not looked at it yet.
I think Kalit also suggested that there's a unit test doing exactly the same thing, which might be… Yes, which might be a good way to troubleshoot the problem.
And… looks like… Yeah, it looks like some, something was found.
If it's… so, for those who don't know, regular expressions are not working everywhere.
So we have a record on some platforms, and that… it looks like it's related to that.
And, this one, this is actually old, I think it's, Yeah, some, some way to provide more options to the single processor and the batch processor.
It, it looks okay.
The thing in that case, I think it would be better if we have a spec for that, because it's… When different, languages and different teams are making the same enhancements, but the spec is not adjusted.
Oh… it's harder to maintain in the long term, but otherwise, the ID is okay, and the suggested code is trivial to be implemented.
Any question on issues?
Okay.
Sorry for the pace, I'm just going quickly, because I have another meeting coming on, so… For PRs, not… so, a few PRs have been merged, so it's, what we have is the very main part.
Some PRs are generated with Copilot, so we are still figuring out how this works.
One competitive PR was merged last week, which is… This one from Nalit, so… At least we can have some… some PR that works, where EZCLD is actually passing.
Oh, it doesn't show anymore, but… so this… so this is a… a PR gene with my co-pilot, and it passed the EZCLE check.
And we have… we have others who trusted work in progress, so, those, those three.
So, it will take some time to figure out how to work with Copilot, it's still… I have not tried it, only let it has tried it so far, I think.
And, just be careful about, accepting suggestions in the code, because that part is not working yet with EZCLA.
So… This is causing a trouble here with, with the PR for moment.
So, we… We'll probably need to, file an OPR, because this part is blocking.
So, that has… this pair is some cleanup which has been reviewed and accepted, but it's, We need to see how to fix the workflow.
So, resource detectors, yes, thanks, Nikhil. So, I will… I will take a look at the comment from Owens and see what we need to do for this Unicode part.
Just to know, oh, and typically uses some very old platforms, so that this might be a reason why, sometime he has some specific, platform requirements on very, very old releases.
So, we'll take a look and see what we need to do.
**Nikhil Bhatia** 13:07 Yeah, so…
**malff** 13:10 Everything else is pretty old, We are still, still need to do some, some cleanup.
Of these at some point.
But no, no urgency on that.
And this is… Pretty much it for, recent peers.
Anything I missed, or that you want to discuss?
Hassan, anything?
**Ehsan** 13:51 No, nothing, thank you. Thanks, Mark.
**malff** 13:53 Yes. Nice, nice to see youth.
Huh.
**Ehsan** 13:57 Beautiful.
**malff** 13:58 And, well, nice to see every one of you, but… So we have, I think Duke, so… It might not be as available as it used to be, like, for 5 months, maybe, but it will be back after that.
And, and Alitz had a conflict today with another conference.
So, yeah, overall, it's looking good, just have to figure out the details for that co-pilot fee.
Last time, I think I mentioned doing another release, so it's, we are in September.
I think there will be probably a release in September sometime, but no… no fixed date yet.
If you… If you need anything, maybe for resource detectors, things like that, we can see, when, when to do the release, so that the important PRs that needs to be there, we can, we can wait for them to do the release.
Otherwise, we can always take the… Oh, merge, merge data.
**Nikhil Bhatia** 15:17 Sorry.
**malff** 15:17 Yes?
**Nikhil Bhatia** 15:18 I would like to add something that, I think this would be the last PR on resource detectors, because, host resource detector and, OS resource detectors. Some PRs are there, which changes the existing semantic convention on them.
**malff** 15:35 So, I think…
**Nikhil Bhatia** 15:36 once those are merged in semantic convention, then we could start working on them.
**malff** 15:44 Okay, sounds good.
Yeah, I've noticed the other changes already merged for resource detectors.
I think that should be the last part, then.
So, it's, the next release is not planned, but it's, it's coming. Speaking of which, There is one change, which has been implemented recently.
So, it's mostly for maintainers, but just something to be aware of.
In the past, When making all of these, we had to change the version number in quite a few files.
For example, in some other files in the API, some in SDK, in CMX, in the Bazel build, a couple of places.
And all this is now automated, with a new magic file.
That was added there, it's, So, there is a tool called Tbump, which has a magic configuration file listing all the place where we need to adjust the version number.
Like this. So, there's a version number in cement lists, and… In this place, we need to address the version.
And… Next time, from this point on, when we need to change a version number, just typing this comment only.
We'll adjust, all the files that need to be touched, so it's, It's a minor change, but it will… it's mostly for maintainers. It helps to maintain the code in a consistent state where we don't forget anything.
So, just mentioning that, if you have not seen that recently.
**Ehsan** 17:37 Yeah, that's cool.
**malff** 17:47 So, yeah, apart from that, I don't have any… any other topics.
Hassan, Nikhil or Raphael, any… Any question? Any comment?
**Nikhil Bhatia** 18:02 No, no questions.
**malff** 18:04 Okay.
**Rafael Roquetto** 18:06 Yeah, nothing.
**malff** 18:08 Okay, so yeah, sorry for the… Yeah, sorry for the short meeting, but I have a conflict, so I need to go now.
Thanks, everyone, for joining.
And, see you… Have you online on… in comments, or see you next weekend.
**Rafael Roquetto** 18:27 Thank you for hosting.
**Ehsan** 18:29 Thank you.
Right.
**malff** 18:31 Bye, everyone.
**Nikhil Bhatia** 18:32 Bye, everyone.
