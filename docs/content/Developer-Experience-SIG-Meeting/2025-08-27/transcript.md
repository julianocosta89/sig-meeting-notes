SIG: Developer Experience SIG Meeting
Date: 2025-08-27
Duration: 20 minutes
Zoom Recording URL: https://zoom.us/rec/share/MwzwQQJyx5uSE8izcBHsdLviBd0rQzMe-Q4F4R5Ik89f5x4ldmPYrSDbnyJCqJpF.Np1TP-vqvSdzj_JE
============================================================

## Zoom Recording Transcript

**Damien Mathieu** 00:39 Hey, good morning.
**Tristan Sloughter** 00:40 Hey.
**Juliano Costa | Datadog** 00:43 Hello there!
**Tristan Sloughter** 00:44 Hey, hey!
But he's here.
**Juliano Costa | Datadog** 00:48 Everyone.
**Tristan Sloughter** 00:49 Good.
**Damien Mathieu** 00:50 Good, how are you?
**Juliano Costa | Datadog** 00:52 Yep.
Ugh.
Holidays was… What's good.
**Tristan Sloughter** 00:58 Good.
**Juliano Costa | Datadog** 00:58 -Oh.
**Tristan Sloughter** 01:01 Let's see… Pulling up the agenda…
… Well, I guess we can kick it off, since it's probably just us three. The…
So, first agenda item is, updates on the blog post. My main thing is that I got some more questions out to
guy at Atlassian, and he got feedback to me. So I've got more information to work off of, because I had some follow-up questions about why they did certain things, and …
How they did certain things, and … So I guess the… Anyway, …
The next question about how we structure these is…
then… so Mastodon is going to meet with us, but you haven't set it up yet?
**Juliano Costa | Datadog** 02:00 Yeah, I sent a message, so I came back from holidays on Monday, and I sent a message to Tim, and I'm just waiting on… on him, like, saying a date.
**Tristan Sloughter** 02:11 Right.
Google.
**Juliano Costa | Datadog** 02:14 He was happy to join and talk. We may need a week or two to get an answer, but….
**Tristan Sloughter** 02:23 That's fine.
Yeah, I think the… I started thinking when we had just… if we just had two, that maybe we should just do it as one blog post, but … if we're back to three, then we should keep it as separate blog posts.
**Juliano Costa | Datadog** 02:37 Okay.
Yeah, and, on the other…
company that I reach out, the… I forgot their name.
**Tristan Sloughter** 02:51 Go skyscan?
**Juliano Costa | Datadog** 02:53 No, from Berlin, that I….
**Tristan Sloughter** 02:55 Boom.
**Juliano Costa | Datadog** 02:56 I reached out.
Never heard back from them, so, yeah.
**Tristan Sloughter** 03:00 legal.
Yeah, I've never….
**Damien Mathieu** 03:04 I mean, there, …
Are we still on, also, to, like, Heroku was also interested, so do we want to keep them in line?
Good fees.
Heroku.
Alex, with Alex Arna.
**Tristan Sloughter** 03:24 Yeah
I have one other company, too, but they haven't gotten back to me a second time after the first time, because when I thought we needed
another one, if Macedon wasn't gonna do it.
**Juliano Costa | Datadog** 03:35 Yeah, I… I think the problem with Heroku is that… They are also big, right?
**Damien Mathieu** 03:43 I mean, it's… yes, it's Salesforce, but we are not Salesforce either.
**Tristan Sloughter** 03:49 But the… their collector deployment's fairly large.
**Damien Mathieu** 03:53 Yes.
**Tristan Sloughter** 03:55 I guess, the quiz, like… There might still be….
**Juliano Costa | Datadog** 03:59 Unique information that we….
**Tristan Sloughter** 04:01 gain from talking to them, so it's like…
Don't want to not do it, but also don't want to have too many blog posts we have to write.
So it's a conundrum there of….
**Juliano Costa | Datadog** 04:13 ….
**Tristan Sloughter** 04:14 What if we combined, like, what if we did, like.
large-scale, blog post, and combine Heroku and Atlassian if they fit in there. They might fit more.
**Damien Mathieu** 04:24 that….
**Tristan Sloughter** 04:24 In smaller areas.
**Damien Mathieu** 04:25 That works for me.
**Tristan Sloughter** 04:26 Yep.
**Juliano Costa | Datadog** 04:27 Yeah, I was about to say that, like, if we interview all of them and then check what is common.
**Tristan Sloughter** 04:35 Mmm.
**Juliano Costa | Datadog** 04:35 And what is unique, and then do some call-outs, like, well, maybe…
show a basic and common setup that most large companies use, and then do some, like, those are unique for each one. So, kind of also showing the community that
…
The cone setup may fit your environment, but you also need to have something that is specific to your use case, so….
Yeah, I don't know.
Good.
**Tristan Sloughter** 05:14 I think it would be good.
**Juliano Costa | Datadog** 05:15 I like, I like that idea, yeah.
On the other hand, I… I also think that having more blog posts,
help, kind of, raising awareness of the work. Like, not just about the work that we are doing, but also about
this initiative of educating folks on real use cases. So, like, you have one, and then a couple of weeks later, we have another one, so people kind of start seeing them.
**Tristan Sloughter** 05:46 Good.
**Juliano Costa | Datadog** 05:47 Publish one, and… That's it, then….
**Tristan Sloughter** 05:51 Yeah, nobody sees it.
Yep. New blog posts on the blog, and yeah, people aren't noticing. That's a good point.
I would like that.
really running… not a running thing where we keep doing it forever, but, like.
Running in the sense that we have it for a number of weeks, so…
So it's like a running sequence, … series.
**Juliano Costa | Datadog** 06:15 -
**Tristan Sloughter** 06:16 Well, yeah, maybe we should talk to them and then decide exactly how we want to structure it after we look at commonalities and differences and…
And I think… I mean, I think once… Once…
We fully write one, the next ones will come out easier, so…
It won't take as long to write them after we get one out.
**Juliano Costa | Datadog** 06:40 Yeah, I think once we figure the structure and stuff, then it's easy, yeah, it's easier.
**Tristan Sloughter** 06:46 Just start pumping them out.
to have, … Wait, who were you talking to at Haruka? What time zone would that be?
**Damien Mathieu** 06:57 It's Alex Arnold, but he is US… I don't know which coast he is, but, one of the four U.S. time zones.
**Tristan Sloughter** 07:07 Okay.
**Juliano Costa | Datadog** 07:07 So easy, too.
**Damien Mathieu** 07:11 I mean, it's… yeah, basically, like, end of European day.
**Tristan Sloughter** 07:17 Yeah.
I mean, I could talk to him.
If, doesn't work for you guys, but…
If they're able to do morning, that would be good.
**Damien Mathieu** 07:27 Yes.
**Tristan Sloughter** 07:28 to join, that'd be perfect.
**Damien Mathieu** 07:30 Yeah, Kitub says, BC, Canada.
**Tristan Sloughter** 07:36 Oh, okay.
Oh, yeah.
**Juliano Costa | Datadog** 07:38 British Columbia is on the other side from you, right?
**Tristan Sloughter** 07:42 do it.
**Juliano Costa | Datadog** 07:44 Yeah, that's Vancouver.
**Tristan Sloughter** 07:45 if you….
**Juliano Costa | Datadog** 07:46 Yeah.
**Tristan Sloughter** 07:48 So it's, you know, a little far out.
**Juliano Costa | Datadog** 07:51 Yeah, that's pretty bad for you.
**Tristan Sloughter** 07:54 unit.
Yeah, if I need to do it, I can. And I want to join anyway, but…
That'd be good.
Are you… do you want to set that up?
Damien, or…?
**Damien Mathieu** 08:14 I… I can, if you think, that… that's better. Yeah, I can think of that.
**Tristan Sloughter** 08:20 Okay. Yes.
Come on.
Great, so after that, we'll… I'm gonna keep…
working on this Atlassian one to…
Now that I have more information to…
Try to get, like, a draft out, and we can…
Even if it's not going first, we can still have something that we work off of.
Help us think about questions to ask and things like that, too.
Is there anything else on the blog post we should discuss?
Because… The other thing I had was…
on last Tuesday, not this Tuesday, I wish I'd made it yesterday in case this came up again. I should check the notes. In the specifications SIG,
there was a question, from a Ruby developer about… metrics and, … like a… Global registration of metrics.
And other… and also… Destroying metrics and…
other API and SDK concerns about the metrics, and how to use them, and how to…
Especially from Ruby.
Some of them were… have commonality with Erlang issues.
So… the… I'd run into him before, and…
It also brought, just to mind.
outside of that, that I think spreads across Every SIG?
or every language implementation, that the metrics API is a little…
Low level. Doesn't have a lot of, …
niceties, and I thought it might be something for… after the blog post, we could discuss if it…
If we wanted to do something, …
more touching the spec versus, you know, what we've been doing so far. ….
**Damien Mathieu** 10:25 I think it would be interesting to know their… more in more details their use case. Destroying metrics.
Seems weird to me.
**Tristan Sloughter** 10:35 We're destroying instruments, but yeah.
**Damien Mathieu** 10:37 Yeah, destroying instruments, seems right to me. It's like, I don't know, if you reload config and maybe disable something, maybe? But yeah. And, the, like, she also posted on the Slack channel, and….
**Tristan Sloughter** 10:52 Similarly, retrieving an instrument, technically, the… I couldn't find that on the spec, but it's….
**Damien Mathieu** 11:02 I mean, it's… there is no specific API, like, API endpoint to reach with an existing instrument.
But the SDK spec says that, basically, if you create an instrument that matches one with a different unit or description, there should be a warning.
seeing that you're duplicating things. And I couldn't find that, but I'm pretty sure I remember that SDKs may return an existing instrument when you ask for one that already exists.
**Tristan Sloughter** 11:37 Yep. Yeah, so… I get the…
The issue we had with that is… instrument creation… so… In our case.
Creating an instrument is slower than looking one up if we do this registration thing, and since we have no globals, there's no way to…
Just create it and store it for later use.
So, unless you're passing it through everywhere, you have no reference to it, unless you can store it in the global registry of sorts.
So we do that, so you can just reference it by name from anywhere in the code.
And it sounds like Ruby wants to do the same thing. I'm surprised by that, because Ruby has globals, but she said….
**Damien Mathieu** 12:30 I mean, we do have a global, it's the meter provider.
It's actually what we do in Go, it's that when we create an instrument, it's stored in the meter provider. And, like, you can make the meter provider global or not, but if it's different meter providers, the metrics, the instruments that are not going to be shared, which makes sense. Right.
And I, so there is something global that can allow retrieving, existing instruments.
**Tristan Sloughter** 13:00 Yeah, we have a global…
So, not a goal, we have a registry per meter provider. Our problem, exactly, is that the meter provider is a process
And getting… you don't wanna…
hit the process to get an instrument, because it…
It can be slow if you're doing it concurrently from all your different locks and everything.
**Damien Mathieu** 13:25 damn.
**Tristan Sloughter** 13:25 So we wanted….
**Damien Mathieu** 13:27 I mean, Ben, the fastest… maybe it's also a question… I don't know if… to be… it's also why I think it would be interesting to have their use case, because I'm not sure…
an API change is required, because really the fastest way to retrieve
for the instrument, then, is to just store it, like, within, like, locally. If you… if you are… if you have a metric for, an HTTP server, then you store the instruments, within the HTTP server, or as a package
Global package variable, or something.
Depending on what you're doing, … but that does not require API changes.
**Tristan Sloughter** 14:06 Right. Yeah, there might be….
**Damien Mathieu** 14:08 In Go, we store instruments in structs all the time.
**Tristan Sloughter** 14:12 Oh, yeah, so like in…
But for, like, an HTTP server, are you storing it with the HTTP server, or with the meter provider and getting it?
**Damien Mathieu** 14:21 No, we store it basically in the hotel HTTP instrumentation. We store it within the structs for hotel HTTP instrumentation.
Yeah, which is… it's a… an HTTP middleware, so it's technically on vServer.
**Tristan Sloughter** 14:37 Gretchen.
Yeah, that… One thing…
one way I was considering that people could have to deal with it was storing it in some kind of way like that, if that was provided by…
… By the instrumentation… by the thing you're instrumenting, their middleware support?
So it also is… Kind of still just… it's just not a…
global registry, because you still have to look it up within that struct. You have to know, I want this one.
So you don't actually have, like, a variable named. I mean, you still have the… you have a name in that struct that you're referencing to grab it, …
So it's like, if you had…
a registry in the same sense. It would work similarly, it's just not global or on the meter provider, it's within the
the… context of the instrumentation library of the HTTP server middleware.
So, it's nicer.
I remember, I think ours was a… issue of… Particularly this instrumentation.
Library telemetry that everybody uses that doesn't have great,
Way to pass through state and context from a…
instrumentation library in it, which is annoying. It's Verity.
Very much, you have to do what you can do with what you get in the…
from the user's, like, event. It's annoying. But that's a separate… that's our problem, not something we solve in…
Hotel. So yeah, I was hoping… I can…
Maybe get them to join the…
the later meeting of this SIG, and discuss more with them.
And try to… because, yeah, I'm pretty sure they don't…
they're not in European time zones, but I'll see, for sure, to make sure the… if one of them is, they can discuss it, so we can get more information and see where to go from there.
I don't think separately from that.
If we can get… if there's any other interest, maybe…
Around other metrics API, like, if there's other interest from…
people in the community around the metrics API.
Something to consider.
just when I look at… others….
**Damien Mathieu** 17:02 Yeah, or….
**Tristan Sloughter** 17:03 Like, misinter.
**Damien Mathieu** 17:04 Yeah, if there are several concerns that can already be tackled by how the API works and kind of, …
ways of doing things. I don't know if it would make sense to have a documentation, or maybe a later blog post, later, because we are already on some blog posts, and let's not do them, like, every day. On something like, good practices for, doing metrics?
**Tristan Sloughter** 17:30 Beautiful.
Yeah.
That'd be interesting, there… one metric's concern going on right now in the community is… I know on…
mobile and… front-end stuff and resources. That might be something….
**Damien Mathieu** 17:47 And there is a spec, change that recommends not doing metrics in,
**Tristan Sloughter** 17:55 Right.
**Damien Mathieu** 17:56 in mobile.
**Tristan Sloughter** 17:57 Yeah, I… I voiced my… concern about that change in the PR, because that never got merged, right?
**Damien Mathieu** 18:07 I don't think it… I mean, I was just away for 3 weeks, so I've….
**Tristan Sloughter** 18:10 Yeah.
**Damien Mathieu** 18:10 of,
**Tristan Sloughter** 18:11 Well, thank you.
**Damien Mathieu** 18:11 quick, quick marking notifications, that's right, so, I don't know, but….
**Tristan Sloughter** 18:17 Hopefully no.
**Juliano Costa | Datadog** 18:17 Select all, my mark has read. Yeah.
**Damien Mathieu** 18:21 Yeah, not all, but anything where I was not pinged was kind of like that, yeah.
**Tristan Sloughter** 18:27 I think you were one of the people who also voiced concern, right?
**Damien Mathieu** 18:30 No, I did not answer.
**Tristan Sloughter** 18:32 I'm there with someone else, though.
Yeah, it just seems…
Yeah, I think we can still do metrics. It's the… there's some backends that are doing stuff like putting every resource as a metric attribute, every resource attribute as a metric attribute, so then it blows up. But you don't have to do that. That's just…
what, like, … like, in Prometheus, it's not even to the default. You have to specifically configure it to put that.
So the cardinality blow-up is… not…
Not a spec, like, it's not part of the spec that says…
every resource attribute is a metric attribute, so, yeah.
**Damien Mathieu** 19:10 Many things that people want matrix for are also just events and could just be spans.
**Tristan Sloughter** 19:16 Yep. Yeah.
**Damien Mathieu** 19:18 There's also that, but yeah, I agree that sometimes there may be…
Good use cases for metrics on… Mobile.
**Tristan Sloughter** 19:26 Yep. Yeah.
**Damien Mathieu** 19:27 I think it's much more rare than on the backend.
**Tristan Sloughter** 19:31 Yeah, it probably is. It just seems like a weird… yeah.
**Damien Mathieu** 19:35 Yeah, what would you count, anyway, yeah.
**Tristan Sloughter** 19:37 Yeah.
I don't know.
I don't do any front-end stuff, so… Interesting, too, though. I find it interesting, because…
They do have a lot of problems that… They're unique to their situation.
**Damien Mathieu** 19:51 Yes, and how do you… like, if you do a metric, how do you handle that that metric has been computed at a specific time, but you could only send it a few hours later? Right. And, like, your graph is going to change over time.
**Tristan Sloughter** 20:03 Yeah.
I got some interesting problems.
So that's good that I've got follow-up to do on that.
We've got follow-up to do on the blog post. … Oops.
Anything else we should discuss now?
Hmm.
And we can… Think back up, online in… next week.
Oop.
**Juliano Costa | Datadog** 20:39 Cool.
**Tristan Sloughter** 20:39 Good to have you back.
See you guys….
**Damien Mathieu** 20:43 Talk to you later.
**Juliano Costa | Datadog** 20:44 Yep.
**Damien Mathieu** 20:44 Bye.
**Juliano Costa | Datadog** 20:45 Yay.
