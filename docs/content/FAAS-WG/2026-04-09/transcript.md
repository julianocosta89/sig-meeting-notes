SIG: FAAS WG
Date: 2026-04-09
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Tyler Benson** 00:58 Greetings!
**Warre Pessers** 01:02 Whoa.
Good morning.
**Tyler Benson** 01:10 How are you on this fine day?
**Warre Pessers** 01:13 I'm good, how are you?
**Tyler Benson** 01:15 Doing pretty well.
Sounds like, serkin's not able to make it today.
**Warre Pessers** 01:24 Yeah.
**Tyler Benson** 01:25 See if there's anyone else that wants to join.
**Warre Pessers** 01:29 Yes.
**Tyler Benson** 02:05 By Lucas?
**Lukas** 02:08 Hi, Tyler.
How's everyone doing?
**Tyler Benson** 02:23 Doing great.
I was sad that I wasn't able to make it to KubeCon this year.
I see all of the posts of people Going in all the talks and stuff.
**Lukas** 02:39 Yeah, it'd be, cool to attend one of those.
Where are they? Are they normally in Europe, or…
**Tyler Benson** 02:48 I think they have, one, in each location per year.
So, one in Europe, one in the U.S.
At different times of the year.
**Lukas** 03:02 I might have seen… is this… actually, is there one in, it's in Minneapolis, right? Or…
**Tyler Benson** 03:13 I'm not sure.
**Lukas** 03:16 I'm actually originally from Minneapolis, so… That'd be kind of… I can probably…
**Tyler Benson** 03:21 Oops.
**Lukas** 03:22 Swing by home, and then also attend that.
Wait, nevermind, I think that was something else. I think, yeah, it looks like it's in… Salt Lake City.
For the North America one.
In November.
**Tyler Benson** 03:54 That'll be a little chilly.
**Lukas** 03:57 Probably.
Anyways, is there anything…
**Tyler Benson** 04:15 Yeah, I think we can get started.
**Warre Pessers** 04:18 Yeah, I guess so. I'll quickly share some stuff.
And I see that I'm sharing… The wrong one for the… Okay, that should be it.
nothing much interesting from my end. I did do some analysis on the transform processor impact. I just finished it up right before this meeting, so… expecting some, interaction from, max and Raphael on that issue, and then I think we can… forward with that one.
thinking… yeah, one big issue that I still want to find time to work on is the integration testing, and I think now that things have stabilized, and I've gotten the security advisories down a lot.
**Tyler Benson** 05:29 Yeah, great job on that, by the way.
Nice progress.
**Warre Pessers** 05:33 Thank you, no worries. So, I'll be happy to, to, put in some more, actually interesting work for the integration test suite and stuff like that.
So that'd be nice. I am planning to go through some of these PRs as well, because I think some of this stuff is… Stale, or outdated, or no longer relevant. But just haven't found the time yet.
And there was something else… oh yeah, so there's also this thing that's been ongoing for a very long time. I guess Tyler will probably remember, that we… at the current moment, still don't have SQS context propagation, for AWS Lambda.
And I have had a PR that is open for a very long time on the JazzContrib repo, but I've met with, the people from the JS SIG yesterday, I joined their meeting, and we talked about some stuff, and I think it's going to, get merged sometime soon now.
**Tyler Benson** 06:49 Sorry, which part do they not have for SQS? I thought that, SQS propagation works as long as you're using, the, X-ray, context propagator.
**Warre Pessers** 07:03 Yeah, not really, but that is indeed currently a requirement to, adhere to the spec.
So I have… changed the PR to include that so that it's fully spec compliant, and then also added, let's call it an experimental feature to, use a globally configured propagator instead, if you want to opt into that. But the issue currently, so there is proper, context propagation implemented for the normal AWS SDK in JavaScript, but due to the way that Lambda works, you need to do some stuff differently, because it… theoretically, it would work, if you don't create, like, the event source mapping and stuff like that, that is the actual proper way to do it in Lambda, and if you would manually go and pull your queue, you would get proper context propagation, and you would see the correct spans and links and stuff like that, but, we'd have, we had to, change some stuff for the Lambda instrumentation, too.
Also added properly there.
**Tyler Benson** 08:28 Okay. It's been a while. I don't really remember all of this stuff anymore very well, so… Yeah, it's… I thought that it was working for everything with, if you're using the X-ray propagator, but I could be wrong.
**Warre Pessers** 08:48 Yeah, it's been an ongoing effort for a long time for the Lambda instrumentation, but I do know that, for example, the Java instrumentation already properly does this. I think Python might as well, not sure, but I, I remember getting some inspiration from, how the Java instrumentation works. I think, that's right.
**Tyler Benson** 09:10 I do remember that conversation, no. I forgot that we never closed the loop on that. Sorry.
**Warre Pessers** 09:15 Yeah, exactly. And it's taken a long time because it wasn't spec compliant and stuff like that, but it appears to, Finally, that we may be, able to get that merged, so that'll be nice.
**Tyler Benson** 09:31 Great.
If you need me to, approve any PRs on that, happy to help. Let me know.
**Warre Pessers** 09:39 Yeah, I'll let you know. I'm currently still waiting for the code owner on the JavaScript side, but he should be taking a look any day now, so…
**Tyler Benson** 09:51 Okay, great.
**Warre Pessers** 09:56 Lucas, do you…
**Lukas** 09:58 Yeah, we should be good with Python.
I'd have to double check if the AWS LAM… like, is this on the receiving end that you're… that you need to… that you're updating? Yep.
**Warre Pessers** 10:12 Because… so, the existing AWS SDK instrumentation, at least for JavaScript, it already properly implements context propagation, so injecting, the context into the message attributes, or into the system attributes, that all works perfectly fine, it's just indeed on the receiving end, that there is a little bit of a gap.
**Lukas** 10:38 Yeah, so… I think, yeah, we might need to actually look at the Python implementation.
Yeah, I can… I can do that. I'm… more familiar with the Python side of things, but I think the… if I remember correctly, the… kind of the… Where it gets a little tricky is that.
