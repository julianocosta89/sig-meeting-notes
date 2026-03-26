SIG: FAAS WG
Date: 2026-03-12
Duration: 12 minutes
Zoom Recording URL: https://zoom.us/rec/share/feiCUpAxmoiwvokv3oFwdqLWrmqenB00-Y0kRuTk1ni3pGq2awbxPFhBWjTsMRQw.4S3KqS6IbrkDu7tq
============================================================

## Zoom Recording Transcript

**Raphael Manke** 00:58 No.
**Ritvick Paliwal** 01:02 Hello.
**Warre Pessers** 01:10 Hello, I didn't notice, anyone else joined today.
I'm just going to give it one more minute, and otherwise we can get started, I guess.
I see Lucas has joined as well, hello.
I think this is the… the first time I've seen you.
**Lukas** 02:06 label.
**Warre Pessers** 02:06 I could not attend the meeting, but… Yeah. Nice to meet you.
**Lukas** 02:11 Yeah, nice to meet, all of you as well.
**Warre Pessers** 02:14 Does this meeting time work for you? Because I think you are in the… Quite a different time zone than most of us, probably.
**Lukas** 02:23 Yeah, I'm at U.S. Eastern, so yeah, that's why, like, sometimes it overlaps with my day job, but I'm actually… right now, I'm actually switching jobs, so I have the week off, so… This works good.
**Warre Pessers** 02:40 Okay.
I'm just going to get started here, then, let me share the… meeting notes, so… For those who've been here before, you know that we use this template. If you want to add something to the agenda, any action meeting, action items or notes for the next meeting, go ahead. You can find the link to this in the invite of the meeting as well, or I can drop it here in the… In the chat if you want, But yeah, go ahead and fill out anything if you want to, for today's meeting. Yeah, I'm sorry, Lucas, but this is, like, the template where you're right now, so you need to, move down. Yeah, exactly.
Okay… so… for me, for today, there's not really much to say. I've really been, doing maintenance on the repo, mainly not much, exciting stuff that I've been able to work on.
One thing that remains, the target, that I want to achieve is that we can introduce a proper integration test suite, but, yeah, as I said, a lot of stuff going on.
And doing the maintenance is taking up most of my free time already, so not much time to work on that.
So, if anyone else, has anything they want to discuss, The floor is yours.
**Raphael Manke** 04:31 Do you have an idea how to build integration tests already, or is it just a requirement that you need to have on.
**Warre Pessers** 04:37 Yeah, so I examined, just using… wait, what's it called again? Local stack, But there's some limitations, meaning we can't properly test the working of the layers with local stack, so it'll have to, like, be an actual, tests that we run on AWS, but that's fine, because we have an account for that, and it doesn't have to be a very complicated integration test, so we'll probably remain well within the free limit, since it'll be just a simple smoke test of some sort.
But, yeah, other than that, no further research or planning has been done.
For these efforts?
**Raphael Manke** 05:24 I can provide AWS credits if we need it.
**Warre Pessers** 05:29 That's, that would be nice, but, I think we are hopefully going to be good as is, with the CNCF-provided account, but yeah, we'll see about the specifics, and, I'll keep this in mind, so that's, Certainly good to know.
Any other, remarks or questions?
**Lukas** 05:53 Yeah, I was just.
**Ritvick Paliwal** 05:54 I would like to introduce…
**Lukas** 05:56 Oh, sorry. Go ahead.
**Ritvick Paliwal** 05:58 Sorry. I would like to introduce myself.
Yeah, so I'm new to this, FAST group. I have joined this for the first time.
I'm coming from AppDynamics, transitioning to Splunk Lambda layers, so we directly consume the hotel lambda distributions, so I'd like to make some contributions here.
And if anyone of you can help me with, getting started on the hotel side, if there are any easy-to-pick-up bugs or maintenance items, I would be happy to pick them up.
**Warre Pessers** 06:31 Sounds great. I'll comb through our issues and stuff that's on my mind, and I'll let you know. So I suppose you're already in the Slack channel as well, then.
**Ritvick Paliwal** 06:44 Yes, I'm already in the hotel fast.
**Warre Pessers** 06:46 Okay, I'll, I'll find you, there then. That's, good to know. Nice to… to see that, there's some new, interested people, want to work with us.
**Ritvick Paliwal** 06:58 Thank you.
**Warre Pessers** 07:00 And then, Lucas, I think you wanted to say something as well?
**Lukas** 07:03 Yeah, I was just gonna mention, yeah, we should… I think, with the integration desks, we should be able to stay within the free tier limits.
I don't know if we want to try to… because the integration test I had in mind is that we would actually try to… have the Lambda export some telemetry.
And then we would verify that the telemetry is present.
**Warre Pessers** 07:24 Yeah, that's a good picture.
**Lukas** 07:26 But unfortunately, yeah, that would maybe require running an EC2 container, or EC2 instance, which we probably want to avoid. So…
**Raphael Manke** 07:36 what? To collect the telemetry data, or…
**Lukas** 07:41 Yeah, I mean, we want to, like… like, we would probably want to actually verify that we're actually able to generate telemetry data, right, when we…
**Raphael Manke** 07:50 I have an idea for that.
**Lukas** 07:52 Yeah, I know, we could probably use, like, ngrok or something to, to, force.
**Raphael Manke** 07:56 You can use AWS itself. AWS accepts, has an OTEL endpoint where you can send the data to, and if you enable transaction search, which is their OTEL version, then all this data will end up in a lock group, so you can actually query a lock group afterwards.
**Lukas** 08:10 Oh, that's awesome. Yeah, and then we can… I'm assuming there's, like, free tiers on that, so…
**Warre Pessers** 08:17 Yeah, okay, that sounds good. I was… personally, my initial idea was to simply use the console exporter and, just, like, base it on, on, the logs that come out of that, but I think this idea is a bit better to see, like.
that we are actually exporting it properly. So that sounds interesting, but I don't have any knowledge of how that works, but that's an interesting idea.
So, yeah, if any of you want to, To engage on that issue, because there is an open issue for it.
Or put your thoughts in there, that would be awesome as well.
Then, Other than that, for today, I don't really have anything useful to say, I think. I'm going through the Dependabots PR slowly but surely. Hope to get some time on my evenings this week to… push those through, and then there's… I know there's some open PRs as well, but there's some requested changes here and there also.
And then maybe Lucas, because I know you're a, you have reviewer, permissions.
I'll just pull up my, I'm already in there.
I just added a very small fix, for this leachy config that would fix the, CI run on, Rafael's PR, so if we can just, get this merged, then we are unblocking his PR as well.
So if you could take a look.
**Lukas** 10:08 Yeah, I just approved it.
**Warre Pessers** 10:09 Okay, great, thanks, and emergency.
**Lukas** 10:13 I'll try to look at other, some of the other open PRs.
When I last checked, there wasn't too many, except for, Rafael's.
**Warre Pessers** 10:27 Yeah, no pressure. I think we are doing alright, and there's also some stuff I'll probably have to close some very old, still-opened PRs, and for the same reason, I'm going to go through all the issues again as well, hopefully this weekend.
See what's still relevant and what isn't, just to clean up some of the… Some of the myths.
I don't know if anyone else.
**Raphael Manke** 10:55 Also…
**Warre Pessers** 10:56 Boop, keep on.
**Raphael Manke** 10:56 quick update on the account ID PRs, that are spread across all the instrumentations.
I got some valid feedback in regards of if we really should build up a dependency to the extension in the different languages, so I'm arguing there, and I also found out that it's possible to derive the account ID from the AWS credentials, so parsing the AWS access key ID would retrieve the account ID as well.
So I'm thinking if, I'm adding a dissolution rather than parsing the sim link value, because then it will be more independent of the extension, and, yeah.
So that's what I'm having in my mind, and I'm thinking if I should add that to resource detectors instead of relying to the sim link.
Yeah. The sim link is still cool to inject it via the environment variables for those instrumentations that have the exec webper, because then those don't need any touching of the instrumentations, but for the compiler languages like Go and the others.NET, it might be better to derive it from the credentials.
**Warre Pessers** 12:09 Yeah, that makes sense.
Yeah.
I know it's a lot of work, but, appreciate what you've been doing on that end.
Then if there's nothing else for today, I think we can end it right here.
So, that was old, and Have a nice day, everyone, or evening, or morning, I don't know, wherever you are. And then, Ridvik, I'll, try to contact you if I know some stuff that you could maybe take a look at, We'll talk more in, in Slack.
**Ritvick Paliwal** 12:48 Sure, thank you.
**Warre Pessers** 12:50 Right, have a nice day.
**Raphael Manke** 12:52 Right?
**Warre Pessers** 12:53 Bye.
**Ritvick Paliwal** 12:54 Thanks, everyone. Bye.
**Lukas** 12:56 Thanks, everyone.
