SIG: Developer Experience SIG Meeting
Date: 2026-03-11
Duration: 12 minutes
Zoom Recording URL: https://zoom.us/rec/share/F0226gKlqbR5kzkd7cfN855zOa0CfQmlwqkGVyODcgmQwpBLtBtoyyJuqdcywQAZ.X_aUOYefADG7bTnV
============================================================

## Zoom Recording Transcript

**Johanna Öjeling** 00:21 There it is.
**Perk (Marcin Stożek) | Elastic Ingest** 00:23 Hello, hello, how are ya?
**Johanna Öjeling** 00:25 Good, thank you, how are you?
**Perk (Marcin Stożek) | Elastic Ingest** 00:27 I'm good.
**Johanna Öjeling** 00:29 Hey, you better.
**Juliano Costa | Datadog** 00:30 Morning.
**Perk (Marcin Stożek) | Elastic Ingest** 00:31 Morning.
**Johanna Öjeling** 00:33 Congrats on opening the PR for the blog post!
**Juliano Costa | Datadog** 00:38 Huh. Yeah, it's a long-weighted one.
like…
when I started writing, we were, like… at the beginning of this year, we ran the survey, and then I had to update last year, January.
No.
**Johanna Öjeling** 00:58 But yeah, it takes time to first conduct the interview, and then write it, and, like, with getting approval and feedback and back and forth, so yeah, it's a long process.
But yeah, I'm looking forward to reading the blog post on the website.
**Juliano Costa | Datadog** 01:15 Yeah, well, we have the preview already live, which is cool, but yeah.
**Johanna Öjeling** 01:22 Oh, yay!
Great, yeah.
**Juliano Costa | Datadog** 01:24 I don't know when that will be published. I know that they have, like, a really…
really long…
queue on the blog, and they do not want to publish a lot of blog posts during the month, so, you know, I think they are.
**Johanna Öjeling** 01:43 Aha, okay.
**Juliano Costa | Datadog** 01:43 Reducing the number of blog posts that they are releasing.
**Johanna Öjeling** 01:47 Okay, I see.
**Juliano Costa | Datadog** 01:50 Cool, so EuroLink has, open load.
Will commit the changes.
Cool.
So… Okay.
**Perk (Marcin Stożek) | Elastic Ingest** 02:11 some updates on the… I have some updates on the front of this discussion that we had last week. Johanna discussed last week with, with Alexander.
Alexander Schwarz from IBM, he's a key clock maintainer, and there is an open telemetry. I basically met him during the,
Auto Unplugged in Brussels, and you know, like, we were just chatting, and he said, like, yeah, we use… we use OpenTelemetra a lot for tracing, and it's really funny how…
You know, they're using tracing more than the OpenTelemmetry Collector does.
And, he said that it's,
Last week, he said that it's okay for them to actually, you know, come to us and talk about it, and then we can create a blog post, and they're actually very, very happy to do so.
I've, I've sent an invite for the… for this recording session.
to… him…
For… let me check that out. I believe that was somewhere in April, 8th of April, during this session.
And he also invited one other… one other person from, Red Hat as well, there, another Kiko maintainer, so we may have…
On the April 8th, two people coming here talking about the key group.
And then we can…
**Johanna Öjeling** 03:31 Oh, that's good.
**Perk (Marcin Stożek) | Elastic Ingest** 03:32 Then we can have a recording, talk about how they use intent, then, you know, work on the blog post.
**Johanna Öjeling** 03:38 -
Nice.
Cool, yes, I should… yeah, should be able to make it there, so I'm, looking forward to also participating in an interview since, yeah, the vlog post I wrote, I watched the recordings afterwards, so…
Oh, very good.
Actually attend this one?
**Perk (Marcin Stożek) | Elastic Ingest** 03:57 Yeah.
And that's an update on my end.
**Johanna Öjeling** 04:05 And, on my end, the Adobe blog post is also ready to be, published.
the Skyscanner one, we're still waiting for their PR department to approve it, but otherwise, yeah, once that's done, it should also, yeah, be good to be published. But I wonder, Juliano,
should… like, when should I open the PR for Adobe? Can I do it, like, anytime? Or, like, after yours has been merged, and the, communication sake will, kind of, decide
when it gets published, or should I wait? Do you know how it works?
**Juliano Costa | Datadog** 04:53 I think if we have all the approvals, we can move on and open the PR, even if mine wasn't merged, but then we just say, hey, this should be merged after that.
**Johanna Öjeling** 05:06 Right. And just so they know.
**Juliano Costa | Datadog** 05:11 Because then they already know that we have the blogs already ready to go, and they can plan accordingly.
**Johanna Öjeling** 05:18 if we…
**Juliano Costa | Datadog** 05:18 do not open the PR, as we haven't till now. They… I think they are aware that we are creating this blog post series, but they…
they maybe didn't take into account when planning the release. So, I think it.
**Johanna Öjeling** 05:36 Hmm.
**Juliano Costa | Datadog** 05:37 Better to have that raised already, and they can learn.
Figure when it's the best day to…
**Johanna Öjeling** 05:43 Okay.
**Juliano Costa | Datadog** 05:44 everything.
**Johanna Öjeling** 05:45 Yeah, done.
**Juliano Costa | Datadog** 05:46 Yeah, that's the meeting notes.
That's Adobe, right?
**Johanna Öjeling** 05:59 Yes.
Correct.
**Juliano Costa | Datadog** 06:19 Are you waiting on a final approval, or…
**Johanna Öjeling** 06:26 For Adobe, or…
**Juliano Costa | Datadog** 06:28 For Adobe, yes.
**Johanna Öjeling** 06:30 No, that one is, approved, yeah.
**Juliano Costa | Datadog** 06:33 Okay, cool.
**Johanna Öjeling** 06:34 So it's just the Skyscaler one.
**Juliano Costa | Datadog** 06:37 Perfect.
**Johanna Öjeling** 06:40 So, yeah, then I'll go ahead and open the PR into OpenTelemetry while.
**Juliano Costa | Datadog** 06:46 Awesome. Okay.
Yeah, you'll see that you'll get a couple of,
GitHub, actions issues. They, they have really good guardrails in the docs.
**Johanna Öjeling** 07:04 Which is cool.
**Juliano Costa | Datadog** 07:05 But it fails a lot, and then you need to… it's good that in the error message, you get, like, the comment that you should run to fix, so it's…
**Johanna Öjeling** 07:15 Hmm…
**Juliano Costa | Datadog** 07:17 Pretty straightforward, but it takes a couple of, commits to actually get to the… Ready to go state.
**Johanna Öjeling** 07:26 Yeah, I can remember that from, yeah, other times when I've committed to that before, it's… yeah. But yeah, on the other hand, they also provide good guidelines for how to fix it, and they have automated lots of stuff, so yeah.
**Juliano Costa | Datadog** 07:39 Yep.
So I just fixed the URNA.
**Johanna Öjeling** 07:50 Oh, thank you!
**Juliano Costa | Datadog** 07:52 And then the pipeline failed, so I already fixed the pipeline.
So… Yeah, now it should be good.
Cool. Any… anything else?
**Perk (Marcin Stożek) | Elastic Ingest** 08:14 I just wanted to ask you how nice you're going to be there at KubeCon, because it's apparently in 2 weeks.
**Johanna Öjeling** 08:20 Yeah, but… no, I'm not going, sadly. No. Are you first going, or…
**Perk (Marcin Stożek) | Elastic Ingest** 08:26 Okay, yeah, yeah, so we are, we are both going, and I'm only mentioning this because we also talked with, with, with Alex from Key Clock, that he's going to be there, so we'll probably meet him.
**Johanna Öjeling** 08:36 Yay! Yeah, nice.
**Perk (Marcin Stożek) | Elastic Ingest** 08:39 Oh, yeah, you would…
**Johanna Öjeling** 08:40 Juliano, you'll be speaking this year, right?
**Juliano Costa | Datadog** 08:44 Yeah, I have a talk, and that's, I need to send the slides in 6 days, so, yeah.
**Johanna Öjeling** 08:51 Oops.
**Juliano Costa | Datadog** 08:52 freaking you out.
**Perk (Marcin Stożek) | Elastic Ingest** 08:53 Good luck with that.
**Johanna Öjeling** 08:55 Yeah, all the best.
**Juliano Costa | Datadog** 08:57 Thank you. They'll pass.
I'm excited about it.
I'm just sad that I found out
Two weeks ago that we won't have, the observatory this year.
**Perk (Marcin Stożek) | Elastic Ingest** 09:13 That's cool. So, that…
**Juliano Costa | Datadog** 09:14 That is, have you been to KubeCon before, Johanna?
**Johanna Öjeling** 09:20 No, I've heard of the observatory, but yeah, please remind me, it's thinking of.
**Juliano Costa | Datadog** 09:25 Yeah, so usually we have, like, a nice booth in the, like, in the sponsors area.
Where we have all the hotel folks.
Getting together, and, like.
It's a kind of a booth for a company, but for hotel. So we do the SIG meetings there, we discuss with folks and users using OTEL, so it's really nice. And this here looks like, Splunk
Because that was always, sponsored by Splan.
Looks like Splunk didn't sponsor, and
I think the problem was that there was no communication about that, because I'm pretty sure other companies would…
take over that, yeah. Like, yeah, let's… I don't know…
Split the bill and have something, because it was a paid area.
So, looks like they're, they're, they're… they didn't do, and as we always had, the observatory.
We didn't… we almost never applied for a project pavilion booth.
which is, like, a desk that you have, and you'll talk about the project. That would be too small for Ulta, but…
would be something. But as we have the observatory, we never applied for that. So, when we found out that the observatory wouldn't be there.
we tried to apply, and the deadline was already passed, so I don't know if there will be a space for a hotel.
Anyway, I know that the community will find a place to… to talk, and we can have a…
An official hotel booth.
But…
**Perk (Marcin Stożek) | Elastic Ingest** 11:15 Yeah, occupy some space. Just bring, you know, other folders or anything.
**Juliano Costa | Datadog** 11:21 Exactly.
But yeah, that's the thing.
I've raised that to…
to my, VP, and maybe we can have something, like, during coupon discuss with other companies. So we… we have a bit of all the companies
Contributing, and then we actually have a community booth As we… we had…
**Johanna Öjeling** 11:49 It's a big project, it's like…
**Juliano Costa | Datadog** 11:52 I don't think there is a project pavilion booth for Kubernetes. It's too big to have, like, just a standing desk.
So, yeah, I don't know how that will… will go, but yeah, anyways, yeah, that's…
**Perk (Marcin Stożek) | Elastic Ingest** 12:05 That is actually a very interesting point that you bring that up. I think, like, we should continue that conversation. Like, let's have it with other companies.
**Juliano Costa | Datadog** 12:13 Yep.
Awesome.
Cool. Ben, if that's it, I…
Hope to see you all next week, ma'am.
**Johanna Öjeling** 12:26 Yep. See you later. See you next week Good night, birthday preparation.
**Juliano Costa | Datadog** 12:29 Right.
**Perk (Marcin Stożek) | Elastic Ingest** 12:30 Yeah. Thank you. Bye.
