SIG: Go Auto-Instrumentation SIG
Date: 2025-09-02
Duration: 11 minutes
Zoom Recording URL: https://zoom.us/rec/share/0mNMzZFKYq_y8mNDjaSIxSp4BufDv6ROBBJd4DyTh7PdMfkgpoFuYs2jotd6qCpx.F71L1g5eTqeY6EKE
============================================================

## Zoom Recording Transcript

**Rafael Roquetto** 01:06 Hey, Mike.
**Mike Dame** 01:09 How's it going?
**Rafael Roquetto** 01:10 Good, how are you?
**Mike Dame** 01:12 Good.
**Rafael Roquetto** 01:14 Did you have a long weekend as well over there? You did, right?
**Mike Dame** 01:17 Yeah, yeah, is it… it's not a holiday for you guys, right?
**Rafael Roquetto** 01:21 It was a holiday here in Alberta, yeah, so… I didn't know until, like, Thursday, so I was very pleased when I found out.
**Mike Dame** 01:30 Yeah, same thing. On Sunday, I was, you know, I had already been checking Slack and stuff, because that's… that's not the weekend for the Israel guys, so sometimes I see messages, and then I realized, oh, I actually have, tomorrow off.
When you're having fun.
Mmm.
Hey, Ron.
**Rafael Roquetto** 01:47 Yeah, that's good.
**Ron Federman** 01:56 Hey, what's up?
**Mike Dame** 01:58 Not much…
**Rafael Roquetto** 02:01 We were just talking about the long weekend. Still recovering, I guess.
Catching up with email, that kind of stuff.
**Ron Federman** 02:12 towards Labor Day, right?
**Rafael Roquetto** 02:14 Yeah.
You're based in Germany, right? Or?
**Ron Federman** 02:21 I'm in England.
**Rafael Roquetto** 02:23 Where?
**Ron Federman** 02:24 In Italy.
**Rafael Roquetto** 02:25 Whoa.
**Ron Federman** 02:27 Yeah.
**Rafael Roquetto** 02:30 Cool?
**Mike Dame** 02:31 Odagos is based out of Israel, the… so… actually, all of our… no, me and Baroon, we have someone in India, and me here in Boston, and the rest is… engineering is all in Israel.
**Rafael Roquetto** 02:43 I see.
For some reason, I thought Germany. Yeah. Cool.
**Ron Federman** 02:51 And the last name is… sounds a little bit German, maybe.
**Mike Dame** 02:56 I mean, we can… but the first time… funny story that I heard, like, Ron and Edin talking, I thought it was a French accent. Like, I had never heard Israeli accents before, and I was like, are these guys… Right? Because there's a little bit of… and I've heard other people say similar things about the Israeli accent, that, like, some of the, enunciation sounds similar to… to French, but I was way off.
Anyway, I think we can… is… do you know if Nicola's, gonna be joining, Raphael?
**Rafael Roquetto** 03:29 I haven't heard anything. Let me… I can ask him.
Let me see something…
**Mike Dame** 03:35 It'll be a quick meeting.
I know Tyler said he's not going to be able to join us.
**Rafael Roquetto** 03:43 Okay.
**Mike Dame** 03:45 We could just go through… the PRs, and I had the… I wanted to talk about LLMD, if anyone had heard about that.
I guess I'll… I'll start then.
Are we… oh, do we have to hit a record? We're recording. Alright, we're good. Does anyone, you know, yeah, make sure you add your names to the… to the notes. Trying to remember what Tyler usually says.
Welcome to the Go Auto Instrumentation SIG.
Looking at our agenda, here, we don't have anything added to it, so if there's anything anyone likes to talk about, feel free to add.
the one thing that I had put in here was, this LLMD project, and let me share my screen, too, to kind of show what I'm talking about.
So, I've been, you know, talking to some people who are working on this project, LLMD, I have a friend who works at Red Hat, is involved in the SIG observability, and basically, if you haven't heard of this project, it's like a, basically a control plane or an operator for, running LLMs, on Kubernetes. And so they have, it's a very early project, it's only at V0.2. Not a lot of people involved from Kubernetes, from Google, from Red Hat, I think it has some momentum behind it, what they're trying to solve here, running private LLMs instead of relying on you know, the alternative is making, like, API calls to ChatGPT, so I think a lot of companies will be doing this, but anyway, their SIG observability is looking at adding things like metrics. Tracing is the big thing that I was recently pulled into.
And so, I linked to their observability SIG for their meetings, for anyone that wants to get involved in that, but basically, I've been kind of proposing, to them that they can use, you know, manual no-op span instrumentation in their code, and then use the OTEL EBPF library to instrument it.
because they're… the overhead is a big thing that they're concerned with in this project. Being LLMs, it's… it's got a lot of that, so, yeah, the EBPF option seems like they're interested in it. What I'm kind of proposing to them is that an end goal for this could be using the, the OpenTeometry Go instrumentation repo that we have, so not the… not OBI, but the library directly, so that they can Build that, specifically tailored to what they want, and also provide us with another perspective and use case on using that library, and kind of, help, sort of.
parallel… drive the designs in parallel for their instrumentation, along with our development of the library, to see another perspective on it, so I think that that kind of is mutually beneficial.
I think in the meantime, kind of prototyping and stuff with Obi or Odagos, or, just the image that we provide in the Go instrumentation would probably be what we use, but that's sort of… the whole background, so no one's really missed much, but I would encourage anyone to, you know, if you're interested, you join… you basically join the Google group, and you'll get invited… an invite from that to the… all of the SIG meetings.
This is on Thursdays, I think, right now, so, Yeah, feel free to join and share some more knowledge about how the, you know, the hotel EBPF options work. There hasn't been a whole lot decided there yet. I linked to the proposal for distributed tracing that they have.
Which is kind of the… the plan, so I've had a couple discussions in here with people on how that library… how our, you know, library works, the options like Bayload and Obi and Odagos are for getting the instrumentation, and yeah, I'd love to have a couple more people involved, so… Just a shout out to that, I guess that's one of the cool use cases that I've seen, even though they're not using it yet, but the plan is to use it, so… Yeah, there's no comments on that, we can move on to… just go through the open PRs quick.
These are all… Depend of… renovate, or… Renovate Updates?
So I don't think we need to go through each one of those. We have ceiling.
**Rafael Roquetto** 08:43 Format.
Yeah, that's me. So… it's… I haven't had the time to iterate this since last… Less meeting, but basically… Just for the record, for whoever is watching the recording, I just need to… Iterate this to… build on Docker… use Docker with Clang from at 19.
To ensure that everyone is using the same tooling. So I just decorize this approach, and then we're good to go. I'll try to get to it into the next meeting.
**Mike Dame** 09:18 Hello?
And then we have this rule from… And moreone… This one seems like it might… Need a bump or another round of review?
Looks like you applied the suggestions.
That Tyler had.
So… I don't know what the status of this is.
I think it might need a changelog or a skip changelog.
Hmm, I guess so.
I hate updating other people's branches.
Yes, favorite thing.
**Rafael Roquetto** 10:01 Yeah.
**Mike Dame** 10:15 So that's that Dependabot, updates.
Nothing else, really. Is there anything else that anyone else wanted to chat about?
Right.
Well, in that case, I guess we can give everyone a lot of time back, not too many updates then. Like I said, please feel free to join the LMDSIG. I'll probably talk about it next week, too, when Tyler's back. I bet he'll be interested, Nicola, too. So, if they don't see the recording.
For sure, check it out, because we could use some help over there, and it'll be a cool project to… You know, show our stuff off.
**Rafael Roquetto** 10:55 Sounds good.
**Mike Dame** 10:59 I'll see you guys soon.
**Rafael Roquetto** 11:00 Thank you.
See you guys!
**Mike Dame** 11:02 Bye.
**Ron Federman** 11:03 Right.
