SIG: Developer Experience SIG Meeting
Date: 2026-01-07
Duration: 16 minutes
Zoom Recording URL: https://zoom.us/rec/share/Jt7tsht5lghfvb5x8f-Dhy6co2vuonv_v0xyOsCOt535ycAjUEnOrdOiF46SrTfR.5G1GRLXiSMOb1qIr
============================================================

## Zoom Recording Transcript

**Johanna Öjeling** 01:12 No.
**Juliano Costa | Datadog** 01:19 Hello, hello!
Good mornings.
**Johanna Öjeling** 01:21 Hey, good morning! How are you?
**Juliano Costa | Datadog** 01:24 Good, good. Happy New Year!
**Johanna Öjeling** 01:26 Yeah, Happy New Year!
**Juliano Costa | Datadog** 01:29 How are you?
**Johanna Öjeling** 01:31 Hey, pardon?
**Juliano Costa | Datadog** 01:32 How are you?
**Johanna Öjeling** 01:33 Yeah, I'm doing well. I just got back from vacation today, so catching up on everything that happened, yeah.
How about you? Have you had some time off?
**Juliano Costa | Datadog** 01:43 Same, first day back at work.
**Johanna Öjeling** 01:47 Okay, yeah.
Morning!
**Juliano Costa | Datadog** 01:49 Morning.
**Johanna Öjeling** 01:52 How are you doing, Tammy?
**Damien Mathieu** 01:54 Good, how are you? Happy New Year.
**Johanna Öjeling** 01:56 Yeah, Happy New Year.
**Juliano Costa | Datadog** 01:57 Happy New Year!
Is it public holiday in Paris, and where are you based, Johanna?
**Johanna Öjeling** 02:08 I'm in Sweden.
**Juliano Costa | Datadog** 02:09 Sweden, is it… was a public holiday yesterday over there?
**Johanna Öjeling** 02:13 Yesterday, yes, that's correct, yeah.
**Juliano Costa | Datadog** 02:15 Cool.
**Johanna Öjeling** 02:16 And your… where are you based?
**Juliano Costa | Datadog** 02:19 I'm in Austria. In Austria, okay. Did you also have a public holiday? Yeah, yeah. Okay.
**Damien Mathieu** 02:30 Oh, it's a public holiday because of, like, the epiphany?
**Johanna Öjeling** 02:36 Yes.
Correct, yeah.
**Juliano Costa | Datadog** 02:43 Oh, I changed my background during my holidays, and now I'm annoyed that I align the frames with the lines, but they are not aligned with my camera, so they look tilted, but they are not, and I'm like, oh god, how am I gonna survive that? I'm just gonna drop my… my own… camera from the… from this zone, otherwise I'm gonna… gonna keep looking at me.
Actually, other frames.
Cool.
So, I… I haven't looked through the… my GitHub notifications yet.
There are a couple of them.
How are we with the MCP repo? Have we created one? Do we already have one?
Or have we decided to…
**Johanna Öjeling** 03:43 I think Tristan opened an issue to create a repo?
But I'm not sure… If it's been addressed already.
**Juliano Costa | Datadog** 03:55 Cool.
Okay.
And I think from the developer experiences part, the only thing that we have on our end is sitting and writing the the blocks?
I think Tristan had something in draft, but he… I think he… didn't share… Us yet?
Let me see… Yep.
he created a tab, and I think he said that he would move the direct that he had to this dock, but he didn't, so I don't know.
Other than that, I don't have much to…
**Johanna Öjeling** 05:07 But, we'll stop… For the bulk post? Or…
**Juliano Costa | Datadog** 05:12 Yeah, not the MCP blog post, I think that was more, oh, I forgot his name.
Great. Holidays are awesome.
Yeah, Pavel, thanks. I think Pavo was, was working on that. The blog post that I mentioned is… so, Damien, myself, and Tristan, we have run a couple of, interviews with end users.
to kind of get how they are deploying the collector in production. And we want to make a series of Blog posts sharing with the community how companies are using the collector in production, because this is what… this was one of the things that we got as feedback on the survey, that the docs are… were lacking real-life scenarios, real-life examples.
We have done the first one, the small company, Mastodon, but we didn't get any feedback from them, so we need their approval to move on.
**Johanna Öjeling** 06:17 But, yup.
Hotel.
**Juliano Costa | Datadog** 06:19 I think that will only happen at Fosden, when Damien and I go together to them and say, hey.
**Damien Mathieu** 06:26 Yes, we were.
**Juliano Costa | Datadog** 06:27 I thought, let's take a look. Yes, we were hoping it wouldn't have to…
**Damien Mathieu** 06:31 go to VAT, but yeah.
**Johanna Öjeling** 06:35 Okay, yeah.
**Juliano Costa | Datadog** 06:37 But we do have a couple of other… yeah, I'll take my bat with me.
we do have a couple of other companies, too.
To… to write about.
But we wanted to start, like, small, medium, then large, and extra large, kind of going through size of companies, but…
**Johanna Öjeling** 07:02 beyond.
**Juliano Costa | Datadog** 07:03 The small one didn't reply, so we just stopped there.
Yes.
**Johanna Öjeling** 07:10 Yeah, okay. Yeah, is there anything I can help with? Any outstanding tasks, or… Or you're mostly waiting for their, you know.
**Juliano Costa | Datadog** 07:24 I don't know, to be honest.
**Johanna Öjeling** 07:26 Yeah.
**Juliano Costa | Datadog** 07:27 I will open the doc and invite you to it, so if you want to take a look at the blog post.
**Johanna Öjeling** 07:36 Oh, nice. Thanks.
**Juliano Costa | Datadog** 07:40 Which mayo would be easier to… To tag you on the… on Google Docs.
**Johanna Öjeling** 07:51 I can… Write my email in the chat.
**Juliano Costa | Datadog** 08:09 Cool.
**Johanna Öjeling** 08:39 Got it, thank you.
**Juliano Costa | Datadog** 08:42 Thank you.
Cool. So, I also added you as a review… on the review tracker list. Any… Any feedback here would be welcome. So, the idea is just to share what they are doing, who are them, and how they are deploying. So, we have The… their whole config?
We want to share, like, what were their pain points, and, their impression… while you're using the collector. I think they are using the collector for… Two, two and a half years already in production, and they did not have any issues with it, so… It's kind of just… showing to the community that they can use the collector in production? I mean, I think most of the community already knows, but…
**Johanna Öjeling** 09:56 No, yeah, that's great, yeah, I'll have a look. Thank you for sharing.
**Juliano Costa | Datadog** 10:00 Cool. Awesome.
Yeah, this is not public yet, because it has some data from Mastodon, so we want them to.
**Johanna Öjeling** 10:07 to review.
**Juliano Costa | Datadog** 10:08 and authorize, so then we can, move to, PR and then, open a… Open up here on the hotel blog, official blog?
**Johanna Öjeling** 10:19 Okay, yeah.
**Juliano Costa | Datadog** 10:20 Opentelemetry.io slash blogs.
**Johanna Öjeling** 10:23 Okay, yeah, and this will be the first in, Yeah, cool. Yeah, I think that will be, highly appreciated. I hear that a lot, too, with, yeah, people kind of missing Reference examples, yes, please clear.
**Juliano Costa | Datadog** 10:39 Yeah, and I know that the end user is, working on a project called Hotel Blueprints.
**Johanna Öjeling** 10:48 Oh,
**Juliano Costa | Datadog** 10:49 So, this will also help, I know that the Damien is more, in communication with Tread, because they just… electrifications.
Yes, I'm a… marked as a lead of that project, I'm working on that with Dan.
**Johanna Öjeling** 11:04 Mmm.
**Juliano Costa | Datadog** 11:05 Awesome.
**Damien Mathieu** 11:08 We wanted to, get the other folks we've been conducting interviews with on board for that, and the only one that I had an answer for is Kyscanner.
Did not hear anything from anyone else.
Maybe we should reach out to more folks at FostDem, if you're fair, which I doubt.
**Juliano Costa | Datadog** 11:28 I won't be at Fosten. I will be in Brussels on Saturday. I'm arriving on Saturday.
**Damien Mathieu** 11:35 What you were attending for them entirely?
**Juliano Costa | Datadog** 11:38 Yeah, no, I'm just attending the… the open op… the hotel… Date.
**Damien Mathieu** 11:46 hotel unplugged.
**Juliano Costa | Datadog** 11:48 Yup.
There was no observability…
**Damien Mathieu** 11:52 No.
**Juliano Costa | Datadog** 11:53 a track, so a room, so I didn't submit anything to the performance, rooms, yeah.
Yep.
as Datadog, we got a couple of talks accepted there, so this was good, but I won't be joining the conference at all, so… And I also noticed that, the Hotel Unplugged will not be at the same venue as the… so, not venue, I think the Fosden is at a university?
**Damien Mathieu** 12:28 Yes, Auton Unplugged is in the Graphana office.
**Juliano Costa | Datadog** 12:33 Is it? Okay.
**Johanna Öjeling** 12:34 No, I think we don't have an office, but we're sponsoring the event, but I think it's taking place at some venue in central Brussels.
**Damien Mathieu** 12:44 Okay, so it's, like, a rented venue. Sorry, I thought… Yeah, exactly. Okay.
**Johanna Öjeling** 12:49 No, yeah, I, yeah, I may be going, so, yeah, maybe soon to do a challenge like event.
**Juliano Costa | Datadog** 12:57 I'm excited about it. I've been bugging Austin for a while already, because they are always doing, like.
Hotel Summit and Hotel Bay events in the U.S.
**Johanna Öjeling** 13:12 And never in Europe?
Yeah.
**Juliano Costa | Datadog** 13:14 So, every time they release a new, hey, open observability, whatever, and I'm like, and when are we… when are we getting this in Europe?
Always bugging them, and yeah, I hope the hotel unplugged is, like.
Sold out and packed, so people see that.
We have interest in having those type of events in here, so…
**Johanna Öjeling** 13:37 Yeah, I agree, it's, it's a picture that… yeah, most of the observability events are in the US, so it's nice, yeah, to have one in Europe this time.
**Juliano Costa | Datadog** 13:49 By the way, any of you got talks at KubeCon in, observability, they, got, the results for yesterday.
**Johanna Öjeling** 14:00 I submitted one, but… Yeah, it was rejected. How about you?
**Juliano Costa | Datadog** 14:06 Yeah, I submitted a bunch and got a bunch of rejections. I have one on waitlist, so let'.
**Johanna Öjeling** 14:13 I… Oh, okay.
**Damien Mathieu** 14:14 I got 3 rejections, for both KubeCon and Observability Day as well.
**Juliano Costa | Datadog** 14:21 Yeah, I have a talk with Yuri from Oli Garden that got in.
at KubeCon, but, observability Day, I didn't get anything.
Yeah, I'll be at CubeConso.
**Johanna Öjeling** 14:33 Yeah, well, congrats on getting that accepted.
**Juliano Costa | Datadog** 14:36 What's a device.
It was a long journey to get there. KubeCon has been rejecting me for a while.
So we're gonna talk about, not about overhead, but about overhead on… and we're gonna focus on spend creation, and the verbosity of spends. So… Mainly, I think… we haven't started building the talk, but we just have the idea.
The idea is to compare, auto-instrumentation and manual instrumentation, and, of course, we will get the… the… the… the extreme difference here with some express instrumentation, auto instrumentation that is super noisy and full of spans, and then see what is the overhead of that, and then do, kind of.
Try to replicate the same amount of information, but in a manual manner, and then see how much we're gonna save on that.
So, we have some data, and we hope we can prove it, so that's… that's… that's gonna be the story, so it's.
**Johanna Öjeling** 15:51 Cool.
**Juliano Costa | Datadog** 15:52 Yeah, it's an interesting talk, so, yeah. Yeah.
**Johanna Öjeling** 15:56 That's exciting.
**Juliano Costa | Datadog** 16:00 Cool.
Well, I… I do not have anything else to talk about. If we do not have anything, I think we can, Go back to… to our catching up.
**Johanna Öjeling** 16:17 So it's like a plan.
**Damien Mathieu** 16:20 Talk to you later, Van.
**Juliano Costa | Datadog** 16:22 Yeah, see you next week.
**Johanna Öjeling** 16:25 Bye.
