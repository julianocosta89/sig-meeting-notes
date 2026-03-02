SIG: Collector SIG
Date: 2025-09-10
Duration: 24 minutes
Zoom Recording URL: https://zoom.us/rec/share/scwc9uk8hEtIodezFLZrk72r-Z6xZ_KG7IvEtgm8QZEAMupOy9B4Xy9TXqs_myuL.Nlm5RU1q3Ln58cbC
============================================================

## Zoom Recording Transcript

**Christos Markou** 02:15 Hey folks.
**Pablo Baeyens** 04:51 I guess we can start?
**Christos Markou** 04:57 Sounds good. Yeah, first,
first and only item is mine. So I would like to share with this group, this effort, to move forward.
The whole stability concept for, auto receivers, auto components in general. So…
I started with, checking, how stability level per metric, could be.
communicated with users, and it seems that, mdata.gen already has the support to define stability level per, per metric, but it was all… it was only used for, internal
metrics of the collector, about collector's health. So I started with the first PR, which is to… which is to use… to expose this information, through the templates to the generated documentation.
And then…
I would… yeah, then we would need to think more. I have some suggestions there on the PR and on the linked issue, how we should proceed. My suggestion would be that then…
We can… Start adding, the baseline stability level, which is development.
for all the metrics that do not explicitly, define stability, then after M.10 is released, we can use this updated version to update
Contributes components.
And, yeah, eventually we can even think of…
making this mandatory, field in the schema, if we agree on this, but I'm not sure yet.
So, yeah.
This will allow us to define better rules about stabilizing components later. It is also linked to the discussion about how we should link metrics of
components receiver specifically to some other conventions, but this discussion will follow. I think this one about stability is less controversial right now, more straightforward. So, yeah, if there are suggestions, comments, or if you can just review this PR, I would appreciate this.
Any comments, questions on this?
**Jade Guiton** 07:36 Looks good.
**Christos Markou** 07:38 Okay, sure.
**Pablo Baeyens** 07:39 Makes sense to me.
**Christos Markou** 07:40 chat.
Sounds good. Thank you.
By the way, there was an attempt by some people, like Damien and Roger, my colleagues, tried recently to experiment with
Weaver, using Weaver to generate, both code and documentation for collector components, instead of using mdataGen. But that's not mandatory for us to proceed here. We can, just leverage the mechanism that mdataGen,
Provides today, and then later, as soon as we have, this
as soon as we have support for exposing stability or semantic conventions compatibility, later we can switch to a different mechanism if we decide on this, but it's not mandatory. Just an FYI, in case you have seen this already.
And go to the next one, I guess, public.
**Pablo Baeyens** 09:01 Yep, so… BHAS has been working on an RFC for… Improving how configuration is merged.
On… So, one of the…
approaches, it's one I suggested on a…
And we discussed it on a previous, electric meeting.
It's using YAML tags, so basically, you would,
use a YAML tag that identifies,
Whether you want to append to a particular list, or you want to, override.
on, there is… I think that this… like…
Would be my preferred approach, but there is one problem,
as mentioned by Bihas on a comment,
Which is that the helm chart and the operator do not preserve YAML tags.
And so… I guess… the… Questions here, are…
Is that something that could be fixed on the help chart and the operator? And, as B has says in the comment, do users from the help chart or the operator
Want this feature? Or, like, deciding how to merge, lists?
**Jade Guiton** 10:38 I guess, preliminary question, do the helm chart and operators support multiple configs that can be merged?
**Mikołaj Świątek** 10:46 No.
**Vihas Makwana** 10:48 No.
**Pablo Baeyens** 10:49 Okay.
**Mikołaj Świątek** 10:49 As of right now, we don't, and we specifically made the change at one point to not have users just stick a bunch of YAML text in our CRDs, we turned them into structured ones.
Because that's just a better user experience. And right now, there's no opportunity to specify anything of your own.
in there.
**Pablo Baeyens** 11:12 under the.
**Mikołaj Świątek** 11:12 And the reason.
**Pablo Baeyens** 11:13 Both of the helmet on the operator?
**Mikołaj Świątek** 11:16 I don't… it depends on which chart, because there's… there's… there's a couple. I think the collector Herm chart might just accept multiple configurations, but anything that uses the operator has the operator behavior, where… where you have to use…
Right. The structured config, and in that case, it doesn't really matter?
Here?
I'd have to… I don't… I don't know if I have, like, a well-reasoned opinion about how this might interact with the operator, if the operator allowed multiple config files. I'd have to think about that and maybe bring it to the…
Operator SIG. That's, like, another very… another very easy question to answer, I think.
**Pablo Baeyens** 12:05 Right,
And then, so do we…
Suggest users to use the operator… Like, is that…
the preferred way of using, the collector on Kubernetes, or…
Do we not have a stance? Like, how many people use the… Helm chart, that is.
possibly affected.
Versus the… the other one, the other options that we offer.
**Mikołaj Świątek** 12:43 a good question that I don't know the answer to. I think the actual film chart maintainers might have a better idea, but, like.
Christos, maybe in there?
**Christos Markou** 12:55 Yeah.
Could I ask you to repeat the question? Because I was chatting with Anduan in the chat. Sure, sure.
Sorry.
**Pablo Baeyens** 13:06 Right, so there's multiple ways of using the collector in Kubernetes that we support. It seems like some of them, allow you to pass, or may allow you to pass multiple
Collector configurations and merge them, and others do not.
like, the operator. Is there, like, a blast option among those, or do we know whether users use more of the operator versus…
Your options?
**Christos Markou** 13:36 Yeah, I don't think that I have, or we can have this answer. I can share what we do, or what I've heard of other vendors doing. So, we as Elastic, we use, the CubeStack, hand chart of OpenTelemetry Collector, which under
yeah, it… which also uses the operator, so it's a helmster that installs the operator, and then the operator also installs the… or manages the collectors. The other way is to use the plain helmster that just installs the collectors, directly, but…
I don't know, if… yeah. Right now, I don't think that we have a way to handle, or upstream, we suggest something like, multiple different configurations, from what I've seen.
**Mikołaj Świątek** 14:26 It's… I think that philosophically, I don't know what is used more. Philosophically.
the difference between these is that if you use the collector Helm chart, that's basically like a thin wrapper. Like, that's just, you know, you use Helm and want to have a collector in Kubernetes, so you use the Helm chart, and that automates certain things for you. But in terms of actually using the features of the collector, you're on your own.
Like, you basically have to figure everything out, and…
in that case, you can… I don't know off the top of my head, but if it doesn't let you pass in multiple configurations in there, then it probably shouldn't be difficult to add that, because, like, that harm chart doesn't really get in your way. Whereas the operator is a lot more opinionated, and it does do things.
like, opening ports automatically for you, or setting air back automatically, depending on what components you might have defined, so you don't have to worry about which permissions you need exactly for, like, Kubernetes processor, or the…
metrics, or the cluster metrics receiver, and so on. And I don't think there's a blessed way. It depends on what you want.
for… I think for users which are new to OpenTelemetry, the kind of more constrained experience is better, because they just don't have to worry about the specific details, but
If someone knows what… knows exactly what they want, and they're comfortable managing it on their own, then on their career, that is perfectly fine. And I think we are.
We have a definite opinion about that one of these methods should be… should subsume the other, or that one of them is,
In, in, like, a use case we would like to discourage.
Does that make sense?
**Pablo Baeyens** 16:27 Yeah, that makes sense.
It seems like we do have some data on the end use, sorry, the collector survey.
And I'm calculating, just… Just out of curiosity…
So, it looks like, if I did my calculations right, 30% of the…
users of the collector in Kubernetes that answer the survey, use the operator.
And
38% use?
AutoCollect for Helm chart, then the rest… Use their own manifests.
So it's, like, pretty spread out.
**Mikołaj Świątek** 17:14 No, so it's comparable in that case, which makes sense to me.
There's probably also, like, a slight skew towards own manifest slash home chart, just because if you start… if you, like, adopted hotel before any of these things were actually, like, reasonably ready to use in production, then you're probably staying on that, because of,
**Pablo Baeyens** 17:35 Yeah, that's fair.
**Mikołaj Świątek** 17:36 Yeah, migration, migration, migrations are scary.
**Jade Guiton** 17:46 Looking at the Helm chart, it looks like the default is to pass in the config in the YAML as well.
So the only way to add multiple configs would be to pass Like, manual config arguments.
Which does seem to be that there's an example showing it, so… It seems…
**Mikołaj Świątek** 18:05 Doesn't it let you… doesn't it let you provide your own config map with the config in there?
**Jade Guiton** 18:10 Yeah, so you can pass in extra command line arguments that refer to an extra volume containing the config map. So you can do it if you really want to.
**Mikołaj Świątek** 18:20 And in that case, it will support the YAML tags perfectly fine, right? Because it's just text.
**Jade Guiton** 18:26 Yeah, presumably.
If it's, if the config map is loaded… Properly, I suppose.
**Mikołaj Świątek** 18:36 To kind of get back to the merging… Proposal.
I can bring this in front of… if you're willing to wait a little bit, I can bring this in front of the operator sake and find out if we have an opinion, but my immediate reaction would be that we're not gonna…
like, this isn't going to interact with what we're doing, most likely, so it shouldn't. So the fact that we don't support it shouldn't block anything in this RFC.
**Pablo Baeyens** 19:09 It would be helpful if we have their opinion, yeah,
But, yeah, I mean, to me… The conversation today was.
strong evidence that we can do this, that we can… we can do the… the ML tags.
**Christos Markou** 19:30 May I ask something, is this use case only for Kubernetes or for all users of the collector?
I assume it's for all users, right?
**Vihas Makwana** 19:40 Yeah, for only.
**Pablo Baeyens** 19:42 Yep.
**Christos Markou** 19:43 Yeah, yeah, maybe… continuing this philosophical, discussion that Mikola started.
In my opinion, we tend to… usually, we tend to push back on features that could be implemented by external dependents, like helm or operators or whatever, but in my opinion, this might be a misunderstanding for people.
Not us, necessarily, but, users or, yeah, people that are using this technology. So…
I, I would…
Yeah, I would propose to consider, like, if we're going to support this at first place in the collector, will benefit all the users.
if we push back on this, and in general, it goes to every kind of feature. We've had similar discussions about the template… templates and how we're going to abstract configurations, and we were raising this always, but why not use Yelm or Customize?
Yeah, probably it is supported by Hell, or you can do things with Hell, but then you push this functionality, and you really end up being dependent on Shell, right? And you cannot support users that are plain, they are not on Kubernetes.
And also, you rely on what Helm will support, or how well an external project will be maintained. So, yeah, that's another perspective, maybe, to put into the table.
**Pablo Baeyens** 21:18 I mean, my… Take with this, which is only slightly related to what you said, is…
We already support this, even if there are other ways of doing it, we may as well support it in a way that is more comfortable for our users, and this seems to be a pain point that users have. So even if…
there's other ways of doing it with, like, help charts or whatnot. We should… Invest on it, since…
It's already something people use.
Anyway, yeah, if you can bring it up on… D… sick on… Just…
Presumably in the PR, let us know, that would be helpful. I'm going to…
to approve the PR, either way, and just…
we can… we can wait a bit more. It's already been open for a long time, so it doesn't matter if we wait one more week.
**Mikołaj Świątek** 22:31 Yeah, operator, operator SIG meeting is tomorrow.
So, by… by Friday, I'll… I'll post on this.
Cool, thank you. Under this pull request, with our comments, if any.
**Vihas Makwana** 23:02 Yeah, so I… I was taking a look at the example shared by Jade, and I think the tags will work fine in this case.
I'll just test it out and confirm it over the PR.
**Pablo Baeyens** 23:32 I…
if somebody complains about Ansible or Puppet, and YAML tags, I'll open an issue on whatever we need to open it. Or Chef, or Solstack, I…
**Mikołaj Świątek** 23:52 But what about said?
**Jade Guiton** 23:58 What about running as a system de-service?
**Pablo Baeyens** 24:08 I'll leave those for… for you all. I haven't worked with those.
Anyway, any… any other topics?
Alright.
Thank you.
See you on the internet.
**Christos Markou** 24:32 Thank you. Bye.
