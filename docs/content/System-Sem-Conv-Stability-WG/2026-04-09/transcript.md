SIG: System Sem Conv Stability WG
Date: 2026-04-09
Duration: 23 minutes
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 03:18 Hello.
**Pablo Baeyens** 03:22 Right.
Let me kick out this.
**Braydon Kains (Google)** 04:12 I can't believe that worked. I just whispered… Chat to fuck off.
And it did.
It said this meeting cannot be recorded because the host has denied permission, and it left.
Nice.
**Pablo Baeyens** 04:27 Okay, nice. I… I just claimed host to kick him out, but…
**Braydon Kains (Google)** 04:32 while I was out.
**Pablo Baeyens** 04:33 That word.
If you… 1, 2, 3… this is the easiest way of doing it, the document idling, you… need to be part of the Open Strategy Calendar Contributors Google Group.
If you're not… just… I guess, asked to join on that link?
And… you just have to go to Participants, Claim Host.
put a key that is on that document I sent on.
You can kick out anybody.
**Braydon Kains (Google)** 05:17 That's okay.
**Christos Markou** 05:19 So you did that this time, or not?
**Pablo Baeyens** 05:21 No, I didn't, I didn't. It was Bradwan's budget, no.
**Christos Markou** 05:25 So, yeah, okay, so this seems faster, what Bryden did.
**Pablo Baeyens** 05:29 Yeah, just general instructions for any bot, but this one seems to be polite.
**Christos Markou** 05:58 I guess, we can start, we don't expect anybody else today.
**Pablo Baeyens** 06:09 Yeah.
I wonder if somebody from the profiling side would be willing to join us on… Talk about, attribute that Bradon asked?
Bye-bye.
**Braydon Kains (Google)** 06:30 Yeah, I didn't get a response in the Slack… I sent a message to them in the Slack channel, the hotel profile Slack channel, and I haven't heard anything back.
to be honest, those attributes haven't changed in ages, so I actually Doubt that they have a concern. They would have a concern with it going for this candidate, but it doesn't feel right for us to just do it without asking them, since they really are… Their attributes more than ours.
**Pablo Baeyens** 07:14 Okay, and… the PR to move.
The executable to its own entity.
Is that ready to be merged?
**Braydon Kains (Google)** 07:28 I think so.
**Donal O'Sullivan** 07:30 Yeah, I think, Braden, you're happy with the feedback, right? So, the last update I did there, I think you approved it, didn't you?
**Braydon Kains (Google)** 07:38 Yep, I did.
And I responded to James' comment, still not really sure I understand what the problem is.
But… I don't think it blocks the PR, in my opinion.
**Donal O'Sullivan** 07:54 Yeah, that's cool, yeah, no, I… yeah, I've seen that. Yeah, I guess he could either join… join this meeting or, create an issue.
Yeah, so we're probably just waiting on… I guess the, semantic conventions merger, right?
**Braydon Kains (Google)** 08:12 So…
**Donal O'Sullivan** 08:13 Yeah, cool. Okay.
I guess all that's left, then, is to create the PR to update the description for the, Build ID, HTL hash.
to make it more generic, and I think… After that, then we can make… credit PR to make the process metrics release candidate, or… what do you think?
**Braydon Kains (Google)** 08:39 I think so.
**Donal O'Sullivan** 08:41 Yeah.
**Dmitrii Anoshin** 08:43 Sounds good to me.
**Donal O'Sullivan** 08:45 Yep.
**Pablo Baeyens** 08:48 I pinged the maintainers to merge the person's executable one.
**Donal O'Sullivan** 09:01 Right.
Thanks, Pablo.
**Pablo Baeyens** 09:15 anything.
**Donal O'Sullivan** 09:15 Yeah, so… well, so as soon as this one is merged, I'll get the other PR up for review.
I'll just… I'll put a message in the, in the Slack channel.
Just to update that description.
That's all the way of…
**Pablo Baeyens** 09:37 Okay, we got a reply from Trask on an issue that… We talk about our Q column, which is this one. This is not for process, but for system.
I guess… One thing that would be useful from the Elastic side is that… I think we've avoided… Having a namespace also be a metric?
I… don't know if… this is still something that we should not do, and I think it was related to something on Elastic Common Schema, that's why I'm asking.
The Elastic, people.
**Christos Markou** 10:32 I think that's not an issue anymore, I can… Ask Alexandra, who used to participate in these discussions, she's a prover for some conventions and double-check.
But, as far as I know, that's not an issue anymore.
**Pablo Baeyens** 10:54 Okay.
That's…
**Christos Markou** 11:02 It's that, issue that I shared, that you shared, 2062, right?
**Pablo Baeyens** 11:08 Right, yeah, so Trask was… Suggesting that we rename system.disk.ios underscore time to system.disk.io.time.
But there's already a system.disk.io metric.
**Christos Markou** 11:27 Okay, cool, I'll send it over to Uti here.
**Pablo Baeyens** 11:40 We could also do something else, that is.
Named differently, but… Honestly, if we can do that, I would prefer Jess.
Replacing the underscores with dots.
**Braydon Kains (Google)** 12:13 That old original rule of, like, the metric cannot also be… A namespace has… Led us to some bad names in the past.
**Pablo Baeyens** 12:23 Yep.
**Braydon Kains (Google)** 12:24 I don't… I don't… Much like system.disk.io.transferred.
It's… it's a fair name, given the rule, but Disk I.O. would be a much nicer name.
**Pablo Baeyens** 12:42 Yeah, let's see what Alexandra says, and if we can… avoided. We… Do so.
Okay, and then one other thing that I had a question about is this issue, 1873… It is labeled as a GA blocker.
I think it would be nice to have this, but I… not convinced that it is a geobooker, but I wanted… Order's opinion.
**Braydon Kains (Google)** 13:23 I… I… think we… talked about this in person? And said that it was okay to not be a GA blocker?
But now I'm trying to remember if that.
**Pablo Baeyens** 13:32 Could be, yeah, I had that big memory, but now I looked at it, and it still had the label, so maybe I just forgot to remove the label.
**Braydon Kains (Google)** 13:41 I am okay with removing the label, for sure. Potentially even closing the issue, but at the very least removing the label.
**Pablo Baeyens** 13:53 Okay, I think we have enough people on the call to… To make that decision.
So then for system, really, the only… I'm looking at the project view.
The only one that is not… Document how to do the transition.
is the dot this, dot… By you.
Thing.
At least from the ones I have on the project, maybe there's something that… Isn't out there.
**Braydon Kains (Google)** 14:53 A lot of those system metrics really haven't changed in a long time, which is probably As good a sign as any, that they're in pretty good shape.
**Pablo Baeyens** 15:18 Alright, I'm sure.
We will find about issues that… We need to address.
That we haven't, but… So far, I guess, we can… we can see what Alexandra says about the… this guy, you'll think I'm… Then, do another pass and see if we missed any… any issues.
**Dmitrii Anoshin** 15:49 Is it… by the way, is it aligned with network? I guess. If we are changing the system, the disk.io, we probably need to do the same for network.
I don't remember what happened.
**Braydon Kains (Google)** 16:04 So I think, I think they're.
**Pablo Baeyens** 16:04 We… sorry, go ahead.
**Braydon Kains (Google)** 16:06 I was gonna say, I think the reason this hasn't come up for network.
yet, is that there's no network I.O. time.
The reason this is becoming a problem is because there's a disk I.O. and a disk I.O. time.
**Dmitrii Anoshin** 16:19 Okay.
**Braydon Kains (Google)** 16:20 But if we do make a change to disk I.O, we should probably make network say the same thing, whatever.
**Dmitrii Anoshin** 16:25 Yeah. That's what I'm saying.
**Christos Markou** 16:30 Oh, now I realize that those are maybe also used by Kubernetes metrics?
Yeah, but it's not an issue, the metrics are not… any close to RC yet, so should be good to change.
**Braydon Kains (Google)** 16:45 Hmm…
**Dmitrii Anoshin** 16:46 We're gonna be… just one comment would result in, like, changing half of the metrics around everything.
**Christos Markou** 16:54 Yeah.
At least we don't need to change it in multiple places. That's good that we have this common registry.
Understand?
**Dmitrii Anoshin** 17:04 I feel that namespacing rule is pretty annoying, because whenever we choose right now how long the metric we end up with, it's still potentially that there is some new variation of every metric.
can be added later on, right? And then we need to, like, figure out some other ways. But if we didn't have that rule.
We might be able to have, like.
The mo- like, the most important.
kind of obvious metric being the same as the namespace, and that should be alright.
In that case, we don't need to change, like, disk I.O.
**Pablo Baeyens** 17:45 Yeah, I hope that the way we resolve this is we… We decide it's fine to have a namespace be equal to a metric, and we don't rename system.disk.io, we just rename.
IO underscore time, 2IO dot time.
**Braydon Kains (Google)** 18:03 Yeah, if I recall, the reason for that issue was something about, like, flattening… The… like, if you have, like, a hierarchical representation of the… of names, and you flatten them, then you don't know how to resolve something that's a namespace and a metric at the same time.
I don't even think I'm explaining it very right, because I never saw a practical version of this that made any sense to me.
**Christos Markou** 18:30 it's every document, JSON-based database, like Mongo, Elasticsearch, everything will… complain in that case, because imagine you have a JSON object thing, and you have the key that is the namespace, and then you try to expand this. It's not possible. That's the flattening issue, practically.
**Braydon Kains (Google)** 18:51 Yeah.
**Christos Markou** 18:51 of this.
**Dmitrii Anoshin** 18:54 Is that something?
**Braydon Kains (Google)** 18:55 The databases are doing?
Like, they'll take a namespace, and then…
**Christos Markou** 19:04 imagine that it's plain JSON thing, doesn't matter if it is for a database or something. You cannot describe this in a JSON, because The key, has to be, like, will have a nested object below.
But then, you cannot attach a single value to this, so that's the collision there.
So that's a hierarchy.
**Dmitrii Anoshin** 19:28 Is there a practical use case to, like, to split the metric by those groups?
by the name…
**Christos Markou** 19:35 Yeah, I think the solution is that, yeah, I think it is fixed by separating the attributes and the resource attributes from the metrics themselves. So, those go to different, let's say, schemas, so there is… they don't belong to the same JSON, path, essentially. That's the… that's the idea.
So it's… it is fixed in this way.
**Dmitrii Anoshin** 20:04 Interesting. Yeah, we… I don't know, it's kind of open and kind of warm, but… White nose. I'm, like, trying it, I don't know.
Or we just rename it to… I would… To be honest, I would be open for renaming it.
But if it just was one metric, right, or two metrics specifically for disk, but it potentially can be… other metrics that needs to be changed to reflect the same pattern. And in that case.
It's gonna be more… maybe more complicated than trying to… Revisit this rule.
But we'll… let's see, maybe it's not that bad of renaming it right now.
**Pablo Baeyens** 21:08 Yeah, here's the list of all the metrics that end.
in .io, there's… I've answered them.
Okay.
Anything… else?
Alright.
See you all next week.
**Dmitrii Anoshin** 21:50 Interest.
**Braydon Kains (Google)** 21:51 Thanks, everyone.
**Donal O'Sullivan** 21:52 Cheers.
